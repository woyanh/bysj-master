import os
import os.path
import re
import sys
import codecs
import base64
import requests
import json
from PIL import ImageDraw,Image

from flask import current_app
from utils import random_filename

def draw_face(img_dir,zb):
    im = Image.open(img_dir)
    draw = ImageDraw.Draw(im)
    for i in range(len(zb)):
        draw.line(((zb[i][1], zb[i][0]), (zb[i][1], zb[i][2])), 'red', 2)
        draw.line(((zb[i][1], zb[i][0]), (zb[i][3], zb[i][0])), 'red', 2)
        draw.line(((zb[i][3], zb[i][2]), (zb[i][3], zb[i][0])), 'red', 2)
        draw.line(((zb[i][3], zb[i][2]), (zb[i][1], zb[i][2])), 'red', 2)
    return im

def save_face(img_dir,zb):
    img = Image.open(img_dir)
    filename = []
    for i in range(len(zb)):
        filename.append(random_filename('.jpg'))
        face = img.crop((zb[i][3], zb[i][0], zb[i][1], zb[i][2]))
        face.save(os.path.join(current_app.config['BYSJ_UPLOAD_PATH'], filename[i]))
    return filename