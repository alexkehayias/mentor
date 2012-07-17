import os
import sys
sys.path.append('/home/dotcloud/current/app')

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings_production'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
