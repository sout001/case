import os
import io
import time


def get_upload_path(self, filename):
    dir_path = time.strftime('%Y/%m/%d')
    ts = str(time.strftime("%Y%m%d%H%M%S"))
    return dir_path + '/' + ts + '/' + '/' + filename


doc = ["docx", "doc", 'txt', 'pdf']
video = ['mp3', 'mp4']


def file_upload_path(self, filename):
    file_type = filename.split(".")[-1]
    if file_type in video:
        file_path = 'video'
    if file_type in doc:
        file_path = 'doc'
    dir_path = time.strftime('%Y/%/%d')
    ts = str(time.strftime("%Y%m%d%H%M%S"))
    return file_path + '/' + dir_path + '/' + ts + '/' + '/' + filename
