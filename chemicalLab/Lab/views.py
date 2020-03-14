from django.shortcuts import render
from django.http import HttpResponse
import thingspeak
import random
import requests
import urllib
import http.client as http
import time
import json


def index (request):
    return HttpResponse('hi')

def send_data(request):
    
    headers = {
     "Content-type" : "application/json"   
    }
    
    dictData = {
        'field1': str(random.randrange(25,30)), 
        'field2' : str(random.randrange(50,80)),
        'field3': str(random.randrange(0,500)),
        'field4': str(random.randrange(500, 510))
        }
    
    requests.post("https://api.thingspeak.com/update?api_key=RYDIXALDBHZQKJOD",data = dictData)
    
    request = requests.get("https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH")
    return HttpResponse(request.text)
# def dummy_data(request):
#     dictData = {
#         'Temperature': str(random.randrange(25,30)), 
#         'Humidity' : str(random.randrange(50,80)),
#         'AQI': str(random.randrange(0,500)),
#         'Lab Number': str(random.randrange(500, 510))
#         }
#     data = json.dumps(dictData)
#     # return(HttpResponse(dictData.items()))
    
#     url = "https://api.thingspeak.com/update?api_key=RYDIXALDBHZQKJOD"
        
#     channel = thingspeak.Channel(
#         1017900,
#         api_key = 'RYDIXALDBHZQKJOD',
#         fmt = 'json',
#         timeout = None,
#         server_url = 'https://api.thingspeak.com/'
#     )
    
#     channel.update(data=data)

#     return HttpResponse(channel.get())

def render_login(request):
    return render(request,"login.html")