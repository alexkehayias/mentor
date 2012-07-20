from django.contrib import admin

from accounts.models import *
from mentorships.models import *

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(JoinRequest)
admin.site.register(Sponsor)
admin.site.register(P2PUProfile)
