import urllib

api_host = 'https://api.qrserver.com/v1/create-qr-code/'

def get_qr_image_url_for_string(value, image_size=150):
    params = {
        'data': value,
        'size': str(image_size) + 'x' + str(image_size)
    }
    return api_host + '?' + urllib.parse.urlencode(params)