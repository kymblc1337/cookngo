from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, add_recipe


class RecipesListView(ListView):
    template_name = "recipes\index.html"
    paginate_by = 2
    cat = None
    def get_context_data(self,  **kwargs):
        context = super(RecipesListView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by("title")
        context["category"] = Category.objects.first()
        return context
    def get_queryset(self):
        return add_recipe.objects.all()

    

