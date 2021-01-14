from django.urls import path
from tree.views import login

urlpatterns = [
    path('login', login),
]
