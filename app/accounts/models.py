from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from mentorships.models import Skill, MentorshipRequest

class P2PUProfile(models.Model):
    user = models.OneToOneField(User)
    p2pu_id = models.CharField(max_length=100)
    picture = models.URLField(null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    skills = models.ManyToManyField(Skill, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return self.user.first_name

class Sponsor(models.Model):
    mentorship_request = models.ForeignKey(MentorshipRequest)
    email = models.EmailField()
    receive_email_updates = models.BooleanField(default=True)

    def __unicode__(self):
        return self.mentorship_request.from_user.first_name

# User model properties

def get_p2puprofile(user):
    # Cache the result so we don't re-run the query every time user.p2puprofile is called
    try:
        return user._get_user_p2puprofile_result
    except AttributeError:
        user._get_user_p2puprofile_result = P2PUProfile.objects.get_or_create(user=user)[0]
        return user._get_user_p2puprofile_result
User.p2puprofile = property(get_p2puprofile)

def send_email(user, subject, content):
    # TODO send notfication API email
    p2pu_id = user.p2puprofile.p2pu_id
    print locals()
    pass
User.send_email = send_email

def send_welcome_email(user, user_type):
    subject = 'Welcome to P2PU Mentorship'
    if user_type == 'student':
        content = render_to_string('email/welcome_student.txt', locals())
    else:
        content = render_to_string('email/welcome_mentor.txt', locals())
    user.send_email(subject, content)
User.send_welcome_email = send_welcome_email

