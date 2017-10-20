from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.messages import error

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
        }
    return render(request,'myapp/index.html', context)


def success(request):
    return render(request, 'myapp/success.html')


def register(request):
    errors = User.objects.validate_reg(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/')
    else:
        # User.objects.create(
        #     first_name=request.POST['first_name'], 
        #     last_name=request.POST['last_name'], 
        #     email=request.POST['email'],
        #     password=request.POST['password'])
        return redirect('/')


def login(request):
    return redirect('/success')