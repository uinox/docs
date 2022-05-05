"""定义learning_logs的URL模式"""
from django.urls import path, re_path
from . import views
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
]