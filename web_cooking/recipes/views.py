from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django import forms
from django.template.context_processors import csrf
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, Recipe, Kitchen, Menu
from django.views import View
from .forms import Add_recipe_form
from django.http import HttpResponseRedirect
from django.db.models import Q

def post_detail(request, id = None):
    obj = get_object_or_404(Recipe, id = id)
    context = {
        "title": obj.title,
        "obj": obj
    }
    return render(request, "recipes/detail.html", context)

def login(request):
    args = dict()
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_errors'] = "Пользователь не найден / неправильный пароль"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def registration(request):
    args = dict()
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        new_userform = UserCreationForm(request.POST)
        if new_userform.is_valid():
            new_userform.save()
            new_user = auth.authenticate(username=new_userform.cleaned_data['username'],password=new_userform.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/')
        else:
            args['form'] = new_userform
    return render_to_response('registration.html', args)


def logout(request):
    auth.logout(request)
    return render(request, "logout.html")

def is_valid_queryparam(param):
    return param != '' and param is not None

class Index(ListView):
    template_name = "recipes\index.html"
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        search_filter = request.GET.get('search')
        menu_id = request.GET.get('menu')
        cous_id = request.GET.get('cousine')
        cat_id = request.GET.get('cat')
        if is_valid_queryparam(search_filter):
            self.recipe_search =  Recipe.objects.filter(title__contains=search_filter)
        else:
            self.recipe_search = Recipe.objects.all()
        if is_valid_queryparam(menu_id):
            menu_filter = Menu.objects.get(pk = menu_id)
            self.recipe_search = self.recipe_search.filter(menu = menu_filter)
        if is_valid_queryparam(cous_id):
            kitchen_filter = Kitchen.objects.get(pk = cous_id)
            self.recipe_search = self.recipe_search.filter(kitchen = kitchen_filter)
        if is_valid_queryparam(cat_id):
            cat_filter = Category.objects.get(pk = cat_id)
            self.recipe_search = self.recipe_search.filter(category = cat_filter)


        return super(Index, self).get(request, *args, **kwargs)


    def get_context_data(self,  **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by("title")
        context["category"] = Category.objects.all()
        context["cousins"] = Kitchen.objects.all()
        context["menues"]  = Menu.objects.all()
        return context

    def get_queryset(self):
        return self.recipe_search


class Add_view(View):
    template_name = 'recipes/add.html'

    def get(self, request, *args, **kwargs):
        form = Add_recipe_form()
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = Add_recipe_form(request.POST or  None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        context = {
            'form': form
        }
        return render(self.request, 'recipes/detail', context)

