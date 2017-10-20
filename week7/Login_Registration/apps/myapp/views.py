from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.messages import error

# Create your views here.
def index(request):
    # context = {
    #     'users': User.objects.all()
    #     }
    return render(request,'myapp/index.html')


def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'myapp/success.html', context)


def register(request):
    errors = User.objects.validate_reg(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message) #, extra_tags=field)
        return redirect('/')
    else:
       
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

