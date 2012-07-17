from django.contrib import admin

from accounts.models import *
from mentorships.models import *

admin.site.register(Mentorship)
admin.site.register(Skill)
admin.site.register(MentorshipRequest)
admin.site.register(Sponsor)
admin.site.register(P2PUProfile)



