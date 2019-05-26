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
            new_post = form.save(commit = False)
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            if 'image' in
            form.image = request.FILES['']
            diff = form.cleaned_data['diff']
            kitchen = form.cleaned_data['kitchen']
            category = form.cleaned_data['category']
            new_post.save()
            Recipe.objects.create(title=new_post.title,
                                  description=new_post.description,
                                  image=new_post.image,
                                  diff=new_post.diff,
                                  kitchen=new_post.kitchen,
                                  category=new_post.category,
                                  )
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

