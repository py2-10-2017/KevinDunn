from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request,'myapp/index.html')


def success(request):
    return render(request, 'myapp/success.html')

def create(request):
    return redirect('/')

def login(request):
    return redirect('/')