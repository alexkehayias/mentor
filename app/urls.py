from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'index.html'}, name='home'),
    url(r'^signup/(?P<user_type>[\w-]+)/$', 'accounts.views.signup', name='signup'),
    url(r'^login/$', 'accounts.views.login', name='login'),   
    url(r'^logout/$', 'accounts.views.logout', name='logout'),   
    url(r'^requests/$', 'accounts.views.project_requests', name='project_requests'),   

    url(r'^mentorship/(?P<mentorship_id>[0-9]+)/log/$', 'mentorships.views.mentorship_log', name='mentorship_log'),   
    
    # Projects
    url(r'^projects/create/$', 'mentorships.views.project_form', name='project_form'),
    url(r'^projects/$', 'mentorships.views.projects', name='project_category'),
    url(r'^projects/skill/(?P<skill_id>[0-9]+)/$', 'mentorships.views.projects', name='project_category_skill'),       
    url(r'^projects/(?P<project_id>[0-9]+)/supporters/$', 'accounts.views.sponsor', name='sponsor'),   
    url(r'^projects/(?P<project_id>[0-9]+)/support/$', 'mentorships.views.support', name='project_support'),   
    url(r'^projects/(?P<project_id>[0-9]+)/$', 'mentorships.views.projects', name='project_detail'),   
    
    url(r'^profile/edit/$', 'accounts.views.profile_form', name='profile_form'),   
    
    url(r'^admin/', include(admin.site.urls)),
)
