from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	response = "Hello, This is a Blog Page Placeholder"
	return HttpResponse(response)

def new(request):
	response = "Forms to create blogs will go here"
	return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, blog_id):
    response = "Display Blog #" + blog_id
    return HttpResponse(response)

def edit(request, blog_id):
    response = "Edit blog #" + blog_id
    return HttpResponse(response)

def destroy(request, blog_id):
    return redirect('/')

