from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Blog

# Create your views here.
def index(request):
	response = "Hello, This is a Blog Page Placeholder"
	return HttpResponse(response)

def update(request):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        return redirect('/blogs')

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

