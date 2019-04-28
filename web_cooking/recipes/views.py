from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.template.context_processors import csrf


def login(request):
    args = dict()
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/test')
        else:
            args['login_errors'] = "Пользователь не найден / неправильный пароль"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return render(request, "logout.html")


def testfunc(request):
    return render(request, "login_complete.html")