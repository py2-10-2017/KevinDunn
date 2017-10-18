from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.messages import error

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request,'users/index.html', context)

def new(request):
	return render(request,'users/new.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/users/new')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/users')

def show(request, id):
    return render(request,'users/show.html', {"users":User.objects.get(id=id)})

def edit(request, id):
    context = {
        'users': User.objects.get(id=id)
    }
    return render(request,'users/edit.html', context)

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/users/new')
    else:
        updating_user = User.objects.get(id=id)
        updating_user.first_name = request.POST['first_name']
        updating_user.last_name = request.POST['last_name']
        updating_user.email = request.POST['email']
        updating_user.save()
        return redirect('/users')

def destroy(request, id):
    removing_user = User.objects.get(id=id)
    removing_user.delete()
    return redirect('/')