from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def register(request):
	response = "Sign in here"
	return HttpResponse(response)

def users(request):
	response = "These are the users..."
	return HttpResponse(response)

def login(request):
	response = "Log in here"
	return HttpResponse(response)

