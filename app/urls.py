from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'index.html'}, name='home'),
    url(r'^signup/(?P<user_type>[\w-]+)/$', 'accounts.views.signup', name='signup'),
    url(r'^login/$', 'accounts.views.login', name='login'),   

    # Mentorship Request
    url(r'^mentorship-request/(?P<step>[\w-]+)/$', 'accounts.views.mentorship_request_form', name='mentorship_request_form'),   
    url(r'^mentorship-request/(?P<step>[\w-]+)/(?P<request_id>[0-9]+)/$', 'accounts.views.mentorship_request_form', name='mentorship_request_form'),
    url(r'^support/(?P<request_id>[0-9]+)/$', 'accounts.views.sponsor', name='sponsor'),   
    url(r'^mentorship-requests/$', 'mentorships.views.mentorship', name='mentorship_category'),
    url(r'^mentorship/(?P<mentorship_id>[0-9]+)/log/$', 'mentorships.views.mentorship_log', name='mentorship_log'),   
    
    # Browse Mentor Requests
    url(r'^mentorship-requests/skill/(?P<skill_id>[0-9]+)/$', 'mentorships.views.mentorship', name='mentorship_category_skill'),       
    url(r'^mentorship-requests/(?P<mentorship_id>[0-9]+)/$', 'mentorships.views.mentorship', name='mentorship_detail'),   
    
    # Mentor Profile
    url(r'^mentor/profile/edit/$', 'accounts.views.mentor_profile_form', name='mentor_profile_form'),   
    
    url(r'^admin/', include(admin.site.urls)),
)
