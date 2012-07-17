from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag()
def server_scheme_and_netloc():
    return settings.SERVER_SCHEME_AND_NETLOC
