from django.shortcuts import render
from django.http import HttpResponse
from . import models as m

"""
To render the pages
"""
def index (request):
    return HttpResponse('hi')

def render_login(request):
    return render(request,"login.html")

"""
To check for something in the database
"""
def login(request):
    if request.user.is_authenticated:
        print(request.user.username)
        try:
            user_data = m.User.objects.get(email = str(request.user.email))
        except m.User.DoesNotExist:
            # user_data = m.User.objects.get(email = "2017.jay.bendre@ves.ac.in")
            return HttpResponse("Hello")
        user_data = user_data.__dict__
        del user_data["_state"]
        print(user_data.items())
        
        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
        return render(request,"index.html",{"user_data" : user_data})
    
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if email != '' or password != '':
            user_data = m.User.objects.get(email = email ,password = password)
            user_data = user_data.__dict__
            del user_data["_state"]
            print(user_data.items())
            
            request.session["email"] = user_data["email"]
            request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
            return render(request,"index.html",{"user_data" : user_data})
    return HttpResponse(request.POST.items())