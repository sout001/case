import os
import io
import time


def get_upload_path(self, filename):
    dir_path = time.strftime('%Y/%m/%d')
    ts = str(time.strftime("%Y%m%d%H%M%S"))
    return dir_path + '/' + ts + '/' + '/' + filename
