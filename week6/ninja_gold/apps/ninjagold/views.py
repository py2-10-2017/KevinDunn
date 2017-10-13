from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random

# Create your views here.
def index(request):
    return render(request, "ninjagold/index.html")

def process(request):
    time = datetime.now().strftime("%Y/%m/%d %-I:%M%p")
    building = request.POST['building']
    try:
        request.session['gold']
        request.session['activites']
    except:
        request.session['gold'] = 0
        request.session['activities'] = []

    if building == "farm":
        amount = random.randint(10,20)
        request.session['gold'] += amount

        request.session['activities'].append("<p>You earned " + str(amount) + " golds from the farm.  (" + time + ")</p>")

    elif building == "cave":
        amount = random.randint(5,10) 
        request.session['gold'] += amount

        request.session['activities'].append("<p>You earned " + str(amount) + " golds from the cave.  (" + time + ")</p>")

    elif building == "house":

        amount = random.randint(2,5) 
        request.session['gold'] += amount

        request.session['activities'].append("<p>You earned " + str(amount) + " golds from the house.  (" + time + ")</p>")

    elif building == "casino":
        amount = random.randint(-50,50) 
        request.session['gold'] += amount

        if amount < 0:
            request.session['activities'].append("<p style='color:red'>Entered a casino and lost " + str(amount) + " golds - (" + time + ")</p>")
        elif amount > 0:
            request.session['activities'].append("<p style='color:green'>You entered a casino and gained " + str(amount) + " golds. (" + time  + ")</p>")
        else:
            request.session['activities'].append("<p>You did't get any gold from the casino. (" + time + ")</p>")

    request.session['gold'] += amount
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')