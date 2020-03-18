from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models as m
from django.contrib.auth import logout

"""
To render the pages
"""
def index (request):
    return HttpResponse('hi')

def render_login(request):
    del request.user
    return render(request,"login.html", {"error" : ""})

"""
To check for something in the database
"""
def login(request):
    if request.user.is_authenticated:
        print(request.user.username)
        try:
            user_data = m.User.objects.get(email = str(request.user.email))
        except m.User.DoesNotExist:
            logout(request)
            # user_data = m.User.objects.get(email = "2017.jay.bendre@ves.ac.in")
            return render(request , "login.html" , {"error" : "User not found"})
        
        user_data = user_data.__dict__
        del user_data["_state"]
        print(user_data.items())
        
        
        return HttpResponse(user_data.items())
        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
        return render(request,"LabOperator/index.html",{"user_data" : user_data})
    
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if email != '' or password != '':
            try:
                user_data = m.User.objects.get(email = email ,password = password)
            except m.User.DoesNotExist:
                return render(request , "login.html" , {"error" : "Invalid Email or password"})
            print("Hi")
            user_data = user_data.__dict__
            del user_data["_state"]
            print(user_data.items())
            
            request.session["email"] = user_data["email"]
            request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
            
            # if user_data["role"] == 0:
            #     pass
            return render(request,"LabOperator/index.html",{"user_data" : user_data})
    else:
        return render(request , "login.html",{"error" : "There has been error in processing your request"})
    
def log_out(request):
    logout(request)
    return redirect("/")