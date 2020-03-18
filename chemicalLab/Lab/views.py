from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models as m
from django.contrib.auth import logout
import requests
import json

"""
To render the pages
"""
def index (request):
    return render(request , "landingpage/landingpage.html")

def render_login(request):
    del request.user
    del request.session
    return render(request,"login/login.html", {"error" : ""})

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
            return render(request , "login/login.html" , {"error" : "User not found"})
        
        user_data = user_data.__dict__
        del user_data["_state"]
        print(user_data.items())
        
        
        return HttpResponse(user_data.items())
        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
        return render(request,"lab_operator/dashboard.html",{"user_data" : user_data})
    
    elif request.session["email"] != None :
        try:
            user_data = m.User.objects.get(email = str(request.session["email"]))
        except m.User.DoesNotExist:
            logout(request)
            # user_data = m.User.objects.get(email = "2017.jay.bendre@ves.ac.in")
            return render(request , "login/login.html" , {"error" : "User not found"})
        
        user_data = user_data.__dict__
        del user_data["_state"]
        print(user_data.items())
        
        last_entry_data = requests.get("https://api.thingspeak.com/channels/1017900/feeds/last.json?api_key=CQ98H95JG2IBYHNH").text
        # return HttpResponse(last_entry_data)
        last_entry_data = json.loads(last_entry_data)        
        # return HttpResponse(last_entry_data.items())
        data = requests.get("https://thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH&results={}".format(last_entry_data["entry_id"])).text
        return HttpResponse(data)
        

        #   return HttpResponse(user_data.items())
        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
        return render(request,"lab_operator/dashboard.html",{"user_data" : user_data})
    
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
            
            if user_data["role_id_id"] == 0:
                pass
            elif user_data["role_id_id"] == 1:
                pass
            else:
                data = requests.get("https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH").text
                return HttpResponse(data.items())
                return render(request,"lab_operator/dashboard.html",{"user_data" : user_data})
    else:
        return render(request , "login/login.html",{"error" : "There has been error in processing your request"})
    
def log_out(request):
    logout(request)
    return redirect("/")