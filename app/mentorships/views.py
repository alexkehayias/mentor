from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import json

from mentorships.models import \
        MentorshipRequest, Mentorship, Skill, MentorshipLog
from mentorships.forms import MentorshipLogForm

@login_required
@csrf_exempt
def mentorship(request, mentorship_id=None, skill_id=None):
    '''View for handling mentorship request category and detail views'''
    if request.method == 'POST':
        mentor = request.user
        user_id = request.POST['user_id']
        skill_id = request.POST['skill_id']
        mentorship_request_id = request.POST['mentorship_request_id']
        student = User.objects.get(p2puprofile__p2pu_id=user_id)
        learning = Skill.objects.get(pk=skill_id)
        Mentorship.objects.get_or_create(
                mentor = mentor, 
                student = student, 
                learning = learning)
        # Close the mentorship request
        mentorship_request = MentorshipRequest.objects.get(pk=mentorship_request_id)
        mentorship_request.closed = True
        mentorship_request.save()
        resp = {'message': 'created'}
        return HttpResponse(json.dumps(resp), mimetype='json')
    if bool(mentorship_id):
        mentorship = get_object_or_404(
                MentorshipRequest, pk=mentorship_id)
        return direct_to_template(request, 'mentorship_detail.html', locals())
    # TODO filter based on reqeusts that are open only
    mentorships = MentorshipRequest.objects.filter(closed=False).select_related('sponsor_set', 'from_user')
    if bool(skill_id):
        skill = Skill.objects.get(pk=skill_id)
        mentorships = mentorships.filter(learning=skill)
    skills = Skill.objects.all()
    return direct_to_template(request, 'mentorship_category.html', locals())

@login_required
def mentorship_log(request, mentorship_id):
    '''Once a mentorship is established, periodic updates 
    track the progress of the mentor -> student relationship'''
    mentorship = Mentorship.objects.get(pk=mentorship_id)
    # TODO handle callback from notifications API
    form = MentorshipLogForm()
    if request.method == 'POST':
        form = MentorshipLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.added_by = request.user
            log.mentorship = mentorship
            log.save()
            saved = True
            form = MentorshipLogForm()
    if request.user == mentorship.student:
        role = "learning"
    else:
        role = "mentoring %s on" % mentorship.student.first_name
    updates = MentorshipLog.objects.filter(mentorship=mentorship)
    return direct_to_template(request, 'mentorship_log.html', locals())
