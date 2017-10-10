from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'survey_app/index.html')

def process(request):
	# if request.method == "POST":
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']

	return redirect('/result')

def result(request):
	
	return render(request, 'survey_app/result.html')
