from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from . import models as m
from django.contrib.auth import logout
import requests
import json
import datetime
import random

"""
To render the pages
"""
def index (request):
    return render(request , "landingpage/landingpage.html")

def render_login(request):
    del request.user
    del request.session
    return render(request,"login/login.html", {"error" : ""})

    
def analysis(request):
    sensor_data = m.Sensor_log.objects.order_by("-timestamp").all()
    # sensor_data = sensor_data.__dict__
    
    
    temperature = []
    humidity = []
    aqi = []
    created_at = []
    lab_count = dict()
    for o in sensor_data:
        # return HttpResponse(o)
        if o.lab_id.id not in lab_count.keys():
            lab_count[o.lab_id.id] = 1
        else:
            lab_count[o.lab_id.id]+= 1
        if len(humidity) == 20:
            break
        temperature.append(
            o.temperature
        )
        
        created_at.append(datetime.datetime.strftime(o.timestamp , "%d %B, %Y %I:%M %p"))
        humidity.append(o.humidity)
        aqi.append(o.air_quality)
        
    lab_labels = [ v for v in lab_count.keys() ]
    lab_data = []
    
    temp_table = zip(temperature , created_at)
    hum_table = zip(humidity , created_at)
    aqi_table = zip(aqi , created_at)
    
    for k,v in lab_count.items():
        lab_data.append(
            {
                "Lab" : k,
                "Count" : v
            }
        )           
    return render(request , "lab_operator/analysis.html" , {"temperature" : temperature , "lab_labels" : lab_labels , "lab_data" : lab_data , "humidity" : humidity,"aqi" : aqi , "created_at": created_at ,
    "temp_table" : temp_table,
    "hum_table" : hum_table,
    "aqi_table" : aqi_table
    })    


def schedule(request):
    return render(request , "lab_operator/schedule.html")

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
        
        
        # return HttpResponse(user_data.items())
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
                return render(request , "login/login.html" , {"error" : "Invalid Email or password"})
            print("Hi")
            user_data = user_data.__dict__
            del user_data["_state"]
            print(user_data.items())
            
            request.session["email"] = user_data["email"]
            request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
            Lab = m.Lab.objects.get(id = user_data["lab_id_id"])
            
            request.session["lab_id"] = user_data["lab_id_id"]
            request.session["lab"] = Lab.name
            if user_data["role_id_id"] == 0:
                pass
            elif user_data["role_id_id"] == 1:
                pass
            else:
                request.session["role"] = "Lab Operator"
                # data = requests.get("https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH").text
                # return HttpResponse(data.items())
                return render(request,"lab_operator/dashboard.html",{"user_data" : user_data})
    
    elif request.session["email"] !=None :
        # return HttpResponse(request.session.items())
        try:
            user_data = m.User.objects.get(email = str(request.session["email"]))
        except m.User.DoesNotExist:
            logout(request)
            # user_data = m.User.objects.get(email = "2017.jay.bendre@ves.ac.in")
            return render(request , "login/login.html" , {"error" : "User not found"})
        
        user_data = user_data.__dict__
        del user_data["_state"]
        print(user_data.items())
        
    
        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
        Lab = m.Lab.objects.get(id = user_data["lab_id_id"])
        
        request.session["lab_id"] = user_data["lab_id_id"]
        request.session["lab"] = Lab.name
        temperature = list()
        created_at = list()
        for i in range(3):
            temp=list()
            for j in range(5):
                temp.append(random.randint(25,35))
            temperature.append(temp)
            
        created_at = ["Monday" , "Tuesday" , "Wednesday" ,"Thursday" , "Friday"]
        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
        return render(request,"lab_operator/dashboard.html",{"user_data" : user_data, "temperature" : temperature, "created_at":created_at })
    
    else:
        return render(request , "login/login.html",{"error" : "There has been error in processing your request"})
    

def get_historic_data(request,id):
    sensor_data = m.Sensor_log.objects.all()
    data = []
    if id == 1:
        for o in sensor_data:
            data.append(
                {
                    "date" : str(o.timestamp),
                    "value" : o.temperature
                }
            )
    elif id ==2 :
        for o in sensor_data:
            data.append(
                {
                    "date" : str(o.timestamp),
                    "value" : o.humidity
                }
            )
    elif id == 3:
        for o in sensor_data:
            data.append(
                {
                    "date" : str(o.timestamp),
                    "value" : o.air_quality
                }
            )
    
    return JsonResponse(data , safe=False)            


def log_out(request):
    logout(request)
    return redirect("/")