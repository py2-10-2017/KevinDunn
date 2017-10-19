from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from django.contrib import messages
from django.contrib.messages import error


def index(request):
    context = {
        'courses': Course.objects.all()
        }
    return render(request,'courses_app/index.html', context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/courses_app')
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        return redirect('/')

    def doublecheck(request):
        return render(request, 'courses_app/remove.html')

    def delete(request, id):
        Course.objects.get(id=id).delete()
        return redirect('/')