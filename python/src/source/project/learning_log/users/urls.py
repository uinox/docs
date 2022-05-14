from django.urls import path, re_path
from django.contrib.auth import login

from . import views

urlpatterns = [
    path('login',views.login,name='login'),
]

app_name='users'