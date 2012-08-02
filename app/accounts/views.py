from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import LoginForm, SponsorForm, ProfileForm
from mentorships.models import Project, JoinRequest

def homepage(request):
    if request.user.is_authenticated():
        return redirect('project_category')
    else:
        return direct_to_template(request, 'index.html', locals())

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user, created = User.objects.get_or_create(
                username = email,
                email = email)
        if created:
            user.set_password(password)
            user.save()
            user.send_welcome_email()
        authenticated_user = authenticate(username=email, password=password)
        auth_login(request, authenticated_user)
    return HttpResponse()

@login_required
def profile_form(request):
    user = request.user
    profile = request.user.p2puprofile
    form = ProfileForm(instance=profile, initial={'first_name':user.first_name, 'last_name':user.last_name})
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('project_form')
    return direct_to_template(request, 'profile_form.html', locals())

def login(request):
    '''Login form'''
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.authenticate(request) == True:
                if request.GET.get('next'):
                    return redirect(request.GET['next'])                        
                return redirect('project_category')
            else:
                form.errors['authenticate'] = "Whoops, wrong email and password!"
    return direct_to_template(request, 'login_form.html', locals())

def logout(request):
    '''Logs out user'''
    auth_logout(request)
    return HttpResponseRedirect('/login/')

def sponsor(request, project_id):
    project = Project.objects.get(pk=project_id)
    form = SponsorForm()
    if request.method == 'POST':
        form = SponsorForm(request.POST)
        if form.is_valid():
            sponsor = form.save(commit=False)
            sponsor.project = project
            sponsor.save()
            form = SponsorForm()
            saved = True
    return direct_to_template(request, 'sponsor.html', locals())

@login_required
@csrf_exempt
def project_requests(request):
    '''View the status of project requests from or for the user'''
    if request.method == 'POST':
        try:
            request_id = request.POST['request_id']
            state = request.POST['state']
        except KeyError:
            return HttpResponseBadRequest()
        project_request = JoinRequest.objects.get(pk=request_id)
        if state == 'accept':
            project_request.accept()
        else:
            project_request.closed = True
            project_request.save()
            print project_request.closed
        return HttpResponse('done')
    user = request.user
    join_requests = JoinRequest.objects
    user_requests = join_requests.filter(added_by=user)
    project_requests = join_requests.filter(project__in=user.project_set.all()).exclude(closed=True)
    return direct_to_template(request, 'requests.html', locals())
