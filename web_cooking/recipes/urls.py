from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from .views import *

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', testfunc),
    url(r'^accounts/login', login),
    url(r'^accounts/logout', logout),
]

#Add Django site authentication urls (for login, logout, password management)
