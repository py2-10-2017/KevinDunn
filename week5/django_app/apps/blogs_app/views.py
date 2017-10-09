from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "Hello, This is a Blog Page Placeholder!"
	return HttpResponse(response)

def new(request):
	response = "Forms to create blogs will go here!"
	return HttpResponse(response)

def show(request, blog_id):
    response = "placeholder to display blog " + blog_id
    return HttpResponse(response)

def edit(request, blog_id):
    response = "placeholder to edit blog " + blog_id
    return HttpResponse(response)

def destroy(request, blog_id):
    return redirect('/')
