from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def home(request):
    return render(request, 'home.html')


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
            except:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        else:
            return render(request, 'singup.html', {
                'form': UserCreationForm,
                'error': 'Password no coinciden'
            })
            
def task(request):
    return render(request, 'task.html')