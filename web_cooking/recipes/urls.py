from . import  views
from django.contrib import admin
from django.urls import path
from .views import login,logout,registration,Add_view,post_update, post_delete

admin.autodiscover()

urlpatterns = [
    path('', views.Index.as_view(), name ="home"),
    path('info/<int:id>', views.post_detail, name = 'detail'),
    path('/login', login),
    path('accounts/logout', logout),
    path('accounts/reg', registration),
    path('add/', Add_view.as_view()),
    path('<int:id>/edit', post_update, name = 'edit'),
    path('delete/<int:id>', post_delete, name = 'delete')
]
