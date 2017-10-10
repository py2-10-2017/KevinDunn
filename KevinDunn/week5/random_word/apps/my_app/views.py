from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random
import string


# Create your views here.
def index(request):
	try:
        request.session['attempt']
    except KeyError:
        request.session['attempt'] = 0

	return render(request, 'index.html', request.session['attempt'], request.session['randword'])


def generate(request):
	allowed_chars = ''.join((string.ascii_letters, string.digits))
	randword = ''.join(random.choice(allowed_chars) for _ in range(14))
	request.session['randword'] = randword
	request.session['attempt'] += 1

	return redirect('/')


def reset(request):
    request.session['attempt'] = 0
    return redirect('/')