from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, add_recipe


class RecipesListView(ListView):
    template_name = "index.html"
    paginate_by = 3
    cat = None
    def get(self, request, *args, **kwargs):
        if self.kwargs['cat_id'] == None:
            cat = Category.objects.first()
        else:
            cat = Category.objects.get(pk = self.kwargs['cat_id'])
        return super(RecipesListView, self).get(request, *args, **kwargs)
    def get_context_data(self,  **kwargs):
        context = super(RecipesListView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.get.order_by("title")
        context["category"] = self.cat
        return context
    def get_queryset(self):
        return add_recipe.objects.filter(category = self.cat).order_by("title")


