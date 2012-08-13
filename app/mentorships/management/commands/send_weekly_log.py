from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models import Q

from datetime import datetime

from mentorships.models import Project

class Command(NoArgsCommand):
    help = "Send weekly reminder to update project pages"

    def handle_noargs(self, **options):
        users = User.objects.filter(is_active=True)
        print datetime.today()
        for user in users:
            projects = Project.objects.filter(Q(members__id=user.id) | Q(added_by=user))
            if projects.exists():
               subject = 'Update progress on your mentorship projects'
               context = {'user': user, 'projects': projects}
               message = render_to_string('email/update_progress.html', context)
               user.send_email(subject, message)
               print 'Notification sent to %s' % user.first_name
        print "Finished sending"
