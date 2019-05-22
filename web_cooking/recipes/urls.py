from . import  views
from django.contrib import admin
from django.urls import path
from .views import login,logout,registration

admin.autodiscover()

urlpatterns = [
    path('', views.Index.as_view(), name ="home"),
    path('info/<int:id>', views.post_detail, name = 'detail'),
    path('accounts/login', login),
    path('accounts/logout', logout),
    path('accounts/reg', registration)
]
