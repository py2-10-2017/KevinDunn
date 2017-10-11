from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request): 
	try: 
		request.session["added_words"]
	except KeyError: 
		request.session["added_words"] = []

	return render(request, 'sw_app/index.html')


def add_word(request):
	add_word = {}
	for key, value in request.POST.iteritems():
		if key != "csrfmiddlewaretoken" and key != "big":
			add_word[key] = value 
		if key == "big":
			add_word["class"] = "big"
		else:
			add_word["class"] = "none"
			
	add_word["the_word"] = request.POST["the_word"]
	add_word["created_at"] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
	
	temp = request.session["added_words"]
	temp.append(add_word)
	request.session["added_words"] = temp

	return redirect('/')


def result(request):
	return redirect('/')

def reset(request):
	for key in request.session.keys():
		del request.session[key]
	return redirect('/')