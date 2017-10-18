from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.messages import error


def index(request):
    
    return render(request,'courses_app/index.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/courses_app')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/courses_app')

    def destroy(request, id):
        return render(request, 'courses_app/remove.html')

    def delete(request, id):
        removing_course = Course.objects.get(id=id)
        removing_course.delete()
        return redirect('/')