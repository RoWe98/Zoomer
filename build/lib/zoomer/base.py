# -*- coding: utf-8 -*-

import cv2
import sys
from urllib import request
import face_recognition


class ZmBase(object):

    def __init__(self,imagePath):

        self.imagePath = imagePath

    def getHaarcascadeFile(self):

        url = "http://qiniusave.luoshaoqi.cn/haarcascade_frontalface_default.xml"

        response = request.urlopen(url)

        html_bytes = response.read()

        with open("haarcascade_frontalface_default.xml",'wb') as fb:
            fb.write(html_bytes)

    def get_platform_judge(self):

        pf = platform.uname()[0]

        if(pf!='windows'):
            return 1
        else:
            return 0