from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Add_recipe

def post_detail(request, id = None):
    obj = get_object_or_404(Add_recipe, id = id)
    context = {
        "title": obj.title,
        "obj": obj
    }
    return render(request, "recipes/detail.html", context)

def post_list(request):
    all = Add_recipe.objects.all
    context = {
        "post_list":all
    }
    return render(request, "recipes/posts.html", context)