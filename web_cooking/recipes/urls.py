from django.conf.urls import url
from . import  views
from django.contrib import admin



urlpatterns = [
    url(r'^(?P<id>\d+)$', views.post_detail, name='detail'),
    url('', views.post_list),
    url(r'^add/$', views.Add_view, name='add')
]