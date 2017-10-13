from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	response = "Here are the surveys!"
	return HttpResponse(response)

def new(request):
	response = "Make a new survey!"
	return HttpResponse(response)