from settings import *
import json

with open('/home/dotcloud/environment.json') as f:
    env = json.load(f)

if env['DOTCLOUD_PROJECT'] == 'mentor':
    SERVER_SCHEME_AND_NETLOC = 'http://mentorship.p2pu.org'
    SERVER_TYPE = 'production'
else:
    SERVER_SCHEME_AND_NETLOC = 'http://mentordev-qu6we2kn.dotcloud.com'
    SERVER_TYPE = 'staging'

EMBED_ANALYTICS = True
DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'template1',
        'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DB_SQL_HOST'],
        'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
        'OPTIONS': {'autocommit': True,}        
    }
}

STATIC_ROOT = '/home/dotcloud/volatile/static/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
