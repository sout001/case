from django.urls import path
from case.views import index_view, play

urlpatterns = [
    path('index', index_view, name='index'),
    path('play', play, name='play')
]
