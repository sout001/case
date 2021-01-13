from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import requests
from urllib import parse


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def play(request):
    return render(request, 'index_form.html')


def download(request):
    rs = requests.get('https://app.onenine.cc/m/api/url/yqd/id/6794OCXgTdmHjbmQtlqWUR1UqxO-repLm79t8g_uP3DTr0CLniTW/format/128000')
    response = FileResponse(rs, content_type='1.png')
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=' + parse.quote('1.mp3', encoding="utf-8")
    return response
