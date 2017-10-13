from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from merchandise import merchandise

# Create your views here.
def index(request):
	if "last_transaction" in request.session.keys():
		del request.session['last_transaction']

	context = {
		'items': merchandise
	}
	return render(request,'amadon_app/index.html', context)


def buy(request, item_id):
	for item in merchandise:
		if int(item_id) == item['id']:  
			purchased = float(request.POST["quantity"]) * float(item["price"])
			how_many = int(request.POST["quantity"])
	try:
		request.session['purchased']
		request.session['how_many']
		request.session['total_amadon']
		
	except KeyError:
		request.session['purchased'] = 0
		request.session['total_items'] = 0
		request.session['total_amadon'] = 0
	
	request.session['purchased'] += purchased
	request.session['how_many'] = how_many
	request.session['last_transaction'] = purchased
	request.session['total_amadon'] += how_many
	return redirect('/checkout')


def checkout(request):
	return render(request, 'amadon_app/checkout.html')


