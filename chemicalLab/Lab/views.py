from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    user_number = m.User.objects.filter(lab_id=request.session["lab_id"]).all()
    user_number = len(user_number)
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
        temperature.append(
            o.temperature
        )
        
        created_at.append(datetime.datetime.strftime(o.timestamp , "%d %B, %Y %I:%M %p"))
        humidity.append(o.humidity)
        aqi.append(o.air_quality)
        
    temp_avg = sum(temperature)/len(temperature)
    humidity_avg = sum(humidity)/len(humidity)
    aqi_avg = sum(aqi)/len(aqi)
    
    temperature = temperature[:20]
    humidity = humidity[:20]
    aqi = aqi[:20]
    
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
    "aqi_table" : aqi_table,
    "temp_avg" : temp_avg,
    "hum_avg" : humidity_avg,
    "aqi_avg" : aqi_avg,
    "user_number" :user_number
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
                request.session["role"] = "Admin"
                return render(request,"admin/dashboard.html",{"user_data" : user_data})
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
        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"]+ " "+ user_data["lname"]
        if user_data["role_id_id"] == 0:
            request.session["role"] = "Admin"
            return render(request,"admin/dashboard.html",{"user_data" : user_data})
        elif user_data["role_id_id"] == 1:
            pass
        else:
            request.session["role"] = "Lab Operator"
            # data = requests.get("https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH").text
            # return HttpResponse(data.items())
            return render(request,"lab_operator/dashboard.html",{"user_data" : user_data})

    
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

@csrf_exempt
def get_schedule_details(request):
    date = request.POST["date"]
    date = datetime.datetime.strptime(date , "%Y-%m-%d")
    schedule_data = m.Schedule.objects.order_by("date").all()
    data = []
    flag = False
    for s in schedule_data:
        s_date = datetime.datetime.strptime(str(s.date) , "%Y-%m-%d")
        if date == s_date:
            flag=True
            user_data = m.User.objects.get(id = s.added_by_id)
            data.append({
                "start_time" : s.start_time,
                "end_time" : s.end_time,
                "description" : s.description,
                "lab_id" : s.lab_id,
                "added_by" : user_data.fname + " "+ user_data.lname,
                "event_type" : s.event_type,
                "title" : s.title,                
            })
    
    if flag:
        return JsonResponse(data,safe=False)
    
    return JsonResponse({"error" : "No events found for the day"})

def log_out(request):
    logout(request)
    return redirect("/")