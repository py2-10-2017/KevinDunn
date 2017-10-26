from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.messages import error
from django.db.models import Count


# ----- Login and Registration ---------------

def index(request):
    context = {
        'users': User.objects.all(),
        }
    return render(request,'myapp/index.html', context)

def register(request):
    result = User.objects.validate_reg(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/')

def login(request):
    result = User.objects.login_val(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')


def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'myapp/reviews.html', context)


def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def user(request, id):
    reviewed_books = Book.objects.annotate(review_count=Count('reviews')).filter(reviews__user_id=id)
    context = {
        'user': User.objects.get(id=id),
        'reviewed_books': reviewed_books
    }
    return render(request, 'myapp/user.html', context)


# ----------- Books and Reviews -------------------------

def reviews(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'recent': Review.objects.recent_and_not()[0],
        'more': Review.objects.recent_and_not()[1]
        }
    return render(request, 'myapp/reviews.html', context)


def book(request, id):
    context = {
        'user_id': request.session['user_id'],
        'book': Book.objects.get(id=id)
    }
    return render(request, 'myapp/book.html', context)


def add(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'myapp/add.html', context)


def create(request):
    errors = Review.objects.validate_review(request.POST)
    if errors:
        for err in errors:
            messages.error(request, err)
    else:
        book=Book.objects.last()
        book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id
        return redirect('/book/{}'.format(book_id))
    return redirect('/add')


def create_additional(request, book_id):
    the_book = Book.objects.get(id=book_id)

    new_book = {
        'title': the_book.title,
        'author': the_book.author.id,
        'rating': request.POST['rating'],
        'review': request.POST['review'],
        'new_author': ''
    }
    errors = Review.objects.validate_review(new_book)
    if errors:
        for err in errors:
            messages.error(request, err)
    else:
        Review.objects.create_review(new_book, request.session['user_id'])
    return redirect('/book/' + book_id)


def delete_review(request, book_id, review_id):
    r = Review.objects.get(id=review_id)
    r.delete()
    return redirect('/book/{}'.format(book_id))
    # deletes that particular record


