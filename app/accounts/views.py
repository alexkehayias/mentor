from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect

from accounts.forms import LoginForm, SponsorForm, MentorProfileForm
from mentorships.models import MentorshipRequest, Skill
from mentorships.forms import MentorRequestForm

def signup(request, user_type):
    '''Create an account for the user that logged in with p2pu
    and create their mentorship request'''
    # TODO decode the login cookie
    user, created = User.objects.get_or_create(
            first_name = 'default',
            last_name = 'default',
            email = 'email@email.com')
    user.send_welcome_email(user_type)
    # TODO scrape profile pages for initial data until we 
    # get a user api from p2pu

    if user_type == 'student':
        return redirect('mentorship_request_form', 'about-me')
    return redirect('mentor_profile_form')

@login_required
def mentorship_request_form(request, step, request_id=None):
    '''Form for creating a new mentorship request'''
    if request.method == 'POST':
        if step == 'about-me':
            form = MentorRequestForm(request.POST)
            if form.is_valid():
                skill_id = request.POST['learning']
                learning = Skill.objects.get(pk=skill_id)
                mentor_request = form.save(commit=False)
                mentor_request.from_user = request.user
                mentor_request.learning = learning
                mentor_request.save()
                return redirect('mentorship_request_form', 'supporters', mentor_request.id)
            else:
                return direct_to_template(request, 'mentorship_request_form.html', locals())
    if step == 'about-me':
        form = MentorRequestForm()
        skills = Skill.objects.all()
        return direct_to_template(request, 'mentorship_request_form.html', locals())
    if step == 'supporters':
        mentorship_request = MentorshipRequest.objects.get(
                pk=request_id)
        return direct_to_template(request, 'get_supporters.html', locals())
    return direct_to_template(request, 'thanks.html', locals())

@login_required
def mentor_profile_form(request):
    profile = request.user.p2puprofile
    form = MentorProfileForm(instance=profile)
    if request.method == 'POST':
        form = MentorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('mentorship_category')
    return direct_to_template(request, 'mentor_profile_form.html', locals())

def login(request):
    '''Login form'''
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.authenticate(request) == True:
                if request.GET.get('next'):
                    if request.GET.get('email_share'):
                        return redirect(request.GET['next']+'?email_share=true')
                    else:
                        return redirect(request.GET['next'])                        
                return redirect('app')
            else:
                form.errors['authenticate'] = "Whoops, wrong email and password!"
    return direct_to_template(request, 'login_form.html', locals())

def sponsor(request, request_id):
    mentorship_request = MentorshipRequest.objects.get(pk=request_id)
    form = SponsorForm()
    if request.method == 'POST':
        form = SponsorForm(request.POST)
        if form.is_valid():
            sponsor = form.save(commit=False)
            sponsor.mentorship_request = mentorship_request
            sponsor.save()
            saved = True
    return direct_to_template(request, 'sponsor.html', locals())
