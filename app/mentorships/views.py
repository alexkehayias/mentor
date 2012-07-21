from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import json

from mentorships.models import \
        JoinRequest, Project, ProjectLog
from accounts.models import Skill
from mentorships.forms import ProjectForm, ProjectLogForm

@login_required
def project_form(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.added_by = request.user
            project.save()
            form.save_m2m()
            return redirect('project_support', project.id)
    return direct_to_template(request, 'project_form.html', locals())

@login_required
@csrf_exempt
def projects(request, project_id=None, skill_id=None):
    '''View for handling mentorship request category and detail views'''
    if request.method == 'POST':
        note = request.POST['note']
        user = request.user
        project = Project.objects.get(pk=project_id)
        # Send a request to join the project
        join = JoinRequest.objects.get_or_create(
                project = project,
                added_by = user,
                note = note)
        join.send_notification()
        resp = {'message': 'created'}
        return HttpResponse(json.dumps(resp), mimetype='json')
    if bool(project_id):
        project = get_object_or_404(Project, pk=project_id)
        return direct_to_template(request, 'mentorship_detail.html', locals())
    # TODO filter based on reqeusts that are open only
    projects = Project.objects.filter(closed=False).select_related('sponsor_set', 'added_by')
    if bool(skill_id):
        skill = Skill.objects.get(pk=skill_id)
        projects = projects.filter(skills=skill)
    skills = Skill.objects.all()
    return direct_to_template(request, 'mentorship_category.html', locals())

@login_required
def support(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return direct_to_template(request, 'get_supporters.html', locals())

@login_required
def mentorship_log(request, project_id):
    '''Once a mentorship is established, periodic updates 
    track the progress of the mentor -> student relationship'''
    mentorship = Project.objects.get(pk=project_id)
    # TODO handle callback from notifications API
    form = ProjectLogForm()
    if request.method == 'POST':
        form = ProjectLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.added_by = request.user
            log.mentorship = mentorship
            log.save()
            saved = True
            form = ProjectLogForm()
    if request.user == mentorship.student:
        role = "learning"
    else:
        role = "mentoring %s on" % mentorship.student.first_name
    updates = ProjectLog.objects.filter(mentorship=mentorship)
    return direct_to_template(request, 'mentorship_log.html', locals())
