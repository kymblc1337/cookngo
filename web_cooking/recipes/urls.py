from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name ="home"),
    path('cat/<int:cat_id>/kit/<int:kitchen_id>/menu/<int:menu_id>/', views.RecipesListView.as_view(), name = "categories"),
]