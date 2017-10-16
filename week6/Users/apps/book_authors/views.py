from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    books = "List of books and authors"
    return HttpResponse(books)