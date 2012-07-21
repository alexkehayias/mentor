from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import LoginForm, SponsorForm, ProfileForm
from mentorships.models import Project, JoinRequest

def signup(request, user_type):
    '''Create an account for the user that logged in with p2pu
    and create their mentorship request'''
    # TODO decode the login cookie
    user, created = User.objects.get_or_create(
            username = 'johnnytest',
            first_name = 'Johnny',
            last_name = 'Test',
            email = 'email@email.com')
    user.set_password('testing')
    user.save()
    user.send_welcome_email(user_type)
    authenticated_user = authenticate(username='johnnytest', password='testing')
    auth_login(request, authenticated_user)
    # TODO scrape profile pages for initial data until we 
    # get a user api from p2pu
    return redirect('profile_form')

@login_required
def profile_form(request):
    profile = request.user.p2puprofile
    form = ProfileForm(instance=profile)
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
                return redirect('')
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
    user_requests = join_requests.filter(added_by=user).exclude(closed=True)
    project_requests = join_requests.filter(project__in=user.project_set.all()).exclude(closed=True)
    return direct_to_template(request, 'requests.html', locals())
