import requests
import urllib

api_host = 'https://artii.herokuapp.com/make/'

def get_ascii_text(value):
    params = {
        'text': value
    }
    request_url = api_host + '?' + urllib.parse.urlencode(params)
    req = requests.get(request_url)
    
    return req.text.replace(' ', '\u00a0') # replacing regular space with nbsp