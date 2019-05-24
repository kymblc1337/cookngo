from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import View
# Create your views here.
from .models import Add_recipe
from .forms import Add_recipe_form

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

class Add_view(View):
    template_name = 'adding_recipe.html'

    def get(self, request, *args, **kwargs):
        form = Add_recipe_form(request.POST or None)
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)
