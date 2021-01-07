import os
import io
import time
import random


def get_upload_path(self, filename):
    dir_path = time.strftime('%Y/%m/%d')
    ts = str(time.strftime("%Y%m%d%H%M%S"))
    return dir_path + '/' + ts + '/' + '/' + filename


doc = ["docx", "doc", 'txt', 'pdf']
video = ['mp3', 'mp4']


def file_upload_path(self, filename):
    dir_path = time.strftime('%Y/%/%d')
    ts = str(time.strftime("%Y%m%d%H%M%S"))
    return dir_path + '/' + ts + '/' + '/' + filename


def stu_id():
    year = time.strftime('%Y')
    number = random.randrange(1000, 9999)
    return "stu" + str(year) + str(number)


def tea_id():
    year = time.strftime('%Y')
    number = random.randrange(1000, 9999)
    return "tea" + str(year) + str(number)
