from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    resp = "user login info"
    return HttpResponse(resp)