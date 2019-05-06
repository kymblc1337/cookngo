from django.urls import path
from . import views
urlpatterns = [
    path('', views.RecipesListView.as_view(), name ="home"),
    path('<int: category_id>/', views.RecipesListView.as_view(), name = "categories"),
]