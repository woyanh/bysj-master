from face import get_access_token,encode
from flask import current_app
import requests


def match(filedir1,filedir2):
    url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    request_url = url + '?access_token=' + get_access_token()
    params = [
        {
            'image': encode(filedir1),
            'image_type': 'BASE64'},
        {
            'image': encode(filedir2),
            'image_type': 'BASE64'
        }]
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    return response.json()
