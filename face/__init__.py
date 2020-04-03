import os
import base64
import requests
import math
from PIL import Image,ImageDraw


request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"


def encode(img_dir):
    f = open(img_dir,'rb')
    base64data = base64.b64encode(f.read())
    base64data = str(base64data,'utf-8')
    return base64data

def get_access_token():
    api_key = 'GcZA890wOUERA3DWDW7XhVz3'
    secret_key = 'txGEDDSemrAEGUuSxM89pI43uc0GZxEd'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + api_key + '&client_secret=' + secret_key
    response = requests.get(host)
    return response.json().get('access_token')

def post_img(token,img,url=request_url):
    request_url = url + "?access_token=" + token
    headers = {'content-type': 'application/json'}
    params = {'image':img,'image_type':'BASE64','max_face_num':'10'}
    response = requests.post(request_url,data=params,headers=headers)
    return response.json()

def draw_face(img_dir,zb):
    im = Image.open(img_dir)
    draw = ImageDraw.Draw(im)
    for i in range(len(zb)):
        draw.line(((zb[i][0],zb[i][1]),(zb[i][2],zb[i][3])),'red',3)
        draw.line(((zb[i][0],zb[i][1]),(zb[i][4],zb[i][5])),'red',3)
        draw.line(((zb[i][2],zb[i][3]),(zb[i][6],zb[i][7])),'red',3)
        draw.line(((zb[i][4],zb[i][5]),(zb[i][6],zb[i][7])),'red',3)
    return im

def get_zb(json):
    zb = json.get('result')
    num_of_face = zb.get('face_num')
    draw_zb = []
    for i in range(num_of_face):
        w = zb.get('face_list')[i].get('location').get('width')
        h = zb.get('face_list')[i].get('location').get('height')
        r = zb.get('face_list')[i].get('location').get('rotation')

        x = zb.get('face_list')[i].get('location').get('left')
        y = zb.get('face_list')[i].get('location').get('top')

        x1 = x + (w*math.cos(-r*(math.pi/180)))
        y1 = y - (w*math.sin(-r*(math.pi/180)))

        x2 = x - (h*math.sin(r*(math.pi/180)))
        y2 = y + (h*math.cos(r*(math.pi/180)))

        x3 = x2 + (w*math.cos(r*(math.pi/180)))
        y3 = y2 + (w*math.sin(r*(math.pi/180)))

        draw_zb.append((x,y,x1,y1,x2,y2,x3,y3))
    return draw_zb

