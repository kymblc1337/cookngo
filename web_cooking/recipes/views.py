from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, Recipe, Kitchen, Menu

def is_valid_queryparam(param):
    return param != '' and param is not None

class Index(ListView):
    template_name = "recipes\index.html"
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        ds = request.GET.get('title_contains')
        if is_valid_queryparam(ds):
            self.recipe_search =  Recipe.objects.filter(title__contains=ds)
        else:
            self.recipe_search = Recipe.objects.all()

        return super(Index, self).get(request, *args, **kwargs)

    def get_context_data(self,  **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by("title")
        context["category"] = Category.objects.first()
        return context

    def get_queryset(self):
        return self.recipe_search

class RecipesListView(ListView):
    template_name = "recipes\filter.html"
    paginate_by = 2
    cat = None
    kit = None
    menu = None
    list_of_cats = dict()
    recipes = None
    def get(self, request, *args, **kwargs):
        cat_id = self.kwargs['cat_id']
        kit_id = self.kwargs['kitchen_id']
        menu_id = self.kwargs['menu_id']
        if cat_id:
            self.cat = Category.objects.get(pk = cat_id)
            self.list_of_cats['category'] = self.cat
        if kit_id:
            self.kit = Category.objects.get(pk = kit_id)
            self.list_of_cats['kitchen'] = self.kit
        if menu_id:
            self.menu = Category.objects.get(pk = menu_id)
            self.list_of_cats['menu']  = self.menu

    def get_queryset(self):
        return Recipe.objects.filter(category=self.cat,menu = self.men, kitchen = self.kit)



    

