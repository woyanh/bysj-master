from face import get_access_token,encode
from flask import current_app
import requests


def search(filedir):
    url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    request_url = url + '?access_token=' + get_access_token()
    img = encode(filedir)
    params = {'image': img, 'image_type': 'BASE64', 'group_id_list': 'class1,class2'}
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    return response.json()
