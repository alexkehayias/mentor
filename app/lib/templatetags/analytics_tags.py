from django import template
from django.utils.safestring import mark_safe

from django.conf import settings

register = template.Library()


@register.simple_tag
def google_analytics_tag():
    if settings.EMBED_ANALYTICS:
        return mark_safe('''
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-33454630-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
        ''')
    else:
        return ''

@register.simple_tag
def event_tracking(category, action, label):
    '''Tag for registering an event with google analytics'''
    if settings.EMBED_ANALYTICS:
        script = mark_safe("_gaq.push(['_trackEvent', '%s', '%s', '%s']);" % (category, action, label))
        return script
    else:
        return ''

