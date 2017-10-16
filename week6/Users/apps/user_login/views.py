from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    resp = "user login info"
    return HttpResponse(resp)

''' Please do the following

Create a new model called 'User' with the information above.
Successfully create and run the migration files
Using the shell...
Know how to retrieve all users.              // from apps.user_login.models import * //
Know how to get the last user.               // 
Create a few records in the users
Know how to get the first user.
Know how to get the users sorted by their first name (order by first_name DESC)
Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. 
    Know how to do this directly in the console using .get and .save.
Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...). '''