from . import  views
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from .views import *



admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^(?P<id>\d+)$', views.post_detail, name = 'detail'),
    url(r'^accounts/login', login),
    url(r'^accounts/logout', logout),
    url(r'^accounts/reg', registration),
]

#Add Django site authentication urls (for login, logout, password management)

