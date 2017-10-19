from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
        }
    return render(request,'myapp/index.html', context)


def success(request):
    return render(request, 'myapp/success.html')


def register(request):
    User.objects.create(
        first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], 
        email=request.POST['email'],
        password=request.POST['password'])
    return redirect('/')


def login(request):
    return redirect('/success')