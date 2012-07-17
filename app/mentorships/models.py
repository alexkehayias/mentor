from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from lib.utils import shorten_url

class MentorshipRequest(models.Model):
    from_user = models.ForeignKey(User)
    learning = models.ForeignKey('Skill')
    so_far = models.TextField(max_length=1000)
    why = models.TextField(max_length=1000)
    closed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-id',)
    def __unicode__(self):
        return self.from_user.first_name
    
    @property
    def share_url(self):
        url = settings.SERVER_SCHEME_AND_NETLOC + '/support/' + str(self.id)
        return shorten_url(url)

class Mentorship(models.Model):
    '''Describes a student/mentor pair'''
    mentor = models.ForeignKey(User, related_name='mentor')
    student = models.ForeignKey(User, related_name='student')
    learning = models.ForeignKey('Skill')
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s: %s learning %s' %(
                self.mentor.first_name, 
                self.student.first_name, 
                self.learning.name)

class MentorshipLog(models.Model):
    '''Describes progress of an established mentorship'''
    mentorship = models.ForeignKey(Mentorship)
    content = models.TextField(max_length=1000)
    added_by = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return self.mentorship.from_user.first_name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
