from django.urls import path
from case.views import index_view, play, download

urlpatterns = [
    path('index', index_view, name='index'),
    path('play', play, name='play'),
    path('download', download, name='download')
]
