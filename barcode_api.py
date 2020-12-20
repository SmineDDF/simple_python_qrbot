import urllib

api_host = 'https://bwipjs-api.metafloor.com/'

def get_barcode_image_url_for_text(value):
    params = {
        'bcid': 'code128',
        'text': value
    }
    return api_host + '?' + urllib.parse.urlencode(params)