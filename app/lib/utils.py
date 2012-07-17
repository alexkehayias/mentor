from django.conf import settings
import urllib
import urllib2
import json

def shorten_url(long_url):
    query_parts = {
        'login': settings.BITLY_LOGIN,
        'apiKey': settings.BITLY_API_KEY,
        'longUrl': long_url,
        }
    query = urllib.urlencode(query_parts)
    bitly_url = 'http://api.bitly.com/v3/shorten?%s' % (query)
    try:
        bitly_response = urllib2.urlopen(bitly_url)
        if bitly_response.getcode() == 200:
            bitly_results = bitly_response.read()
        else:
            return long_url  # TODO: handle error
    except Exception:
        return long_url  # TODO: handle error
    else:
        json_results = json.loads(bitly_results)
        if json_results['status_code'] == 200:
            return json_results['data']['url']
        else:
            return long_url  # TODO: handle error
