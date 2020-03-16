import requests
import time
import random

while True :
    headers = {
    "Content-type" : "application/json"   
    }

    #Sensor data here 
    #Dont change anything else
    # username : 2017.jay.bendre@ves.ac.in
    # password : Bruno@12345
    
    dictData = {
        'field1': str(random.randrange(25,30)), 
        'field2' : str(random.randrange(50,80)),
        'field3': str(random.randrange(0,500)),
        'field4': str(random.randrange(500, 510))
        }

    print(dictData.items())
    
    requests.post("https://api.thingspeak.com/update?api_key=RYDIXALDBHZQKJOD",data = dictData)

    request = requests.get("https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH")
    print(request.text)
    
    time.sleep(10)