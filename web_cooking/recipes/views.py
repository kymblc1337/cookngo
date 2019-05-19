
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django import forms
from django.template.context_processors import csrf
from .models import Add_recipe

def post_detail(request, id = None):
    obj = get_object_or_404(Add_recipe, id = id)
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

