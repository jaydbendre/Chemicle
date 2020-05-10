from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Lab import models as m
import datetime, requests
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

"""
Certain key functions that you can use in backend coding.

1. For Rendering content , return Jsons
    a. render(request,'template_name.html',data) :- data has to be a dictionary, Sometimes the dictionary doesnt get passed and the solution to that 
    is generally to pass {"data" : data} instead of data.
    
    b.HttpResponse("html code goes here") :- renders whatever html code you right on the same URL as you operating on (useful for testing )
    
    c. JsonResponse(dictionary , safe=False):- we send a dictionary as a JSON but it really is not one and hence passing safe=False is essential,
                                                to avoid this , use json module and json.dumps() to convert it into a JSON and send the dictionary
                                                as it is.
                                                
2. Models 
    a. Models have been imported as 'm'. To access models , m.Modelname
    b. To access data from a model we generally use the following line :
        var_name = m.ModelName.objects.get() for one object return
        var_name = m.ModelName.objects.all() for all values in the table
        var_name = m.ModelName.objects.filter(condition).all() for conditional select
    
    c. To access the values within the retrieved model , 
        Case 1: Single Object aka get()
            var_name.attr name helps to access the variable.
        
        Case 2: Multiple objects aka all() or filter().all()
            It returns an array of objects of model , to access content within them , send the array in a for loop and access as :
            
            for var in var_name:
                var.attr to access variable
    
    d. Alternative way to access data in a model is to convert the object to a dictionary , to do that :
        var_name = var_name.__dict__

3. API calls to other sites from backend(highly unlikely to be required but still ):
    Using urllib2 library , documentation is easy to understand.
"""


def dashboard(request):
    return render(request, 'incharge/dashboard.html')


def schedule(request):
    lab_operator = m.User.objects.get(id=10000)
    user_data = m.User.objects.get(email=request.session["email"])
    # m.Notification.create_notification(
    #     to=lab_operator,
    #     by=user_data,
    #     description="This is a new notification",
    #     category=0,
    #     # data = 0
    # )
    return render(request, 'incharge/schedule.html', {"error": '', "success": ""})

@csrf_exempt
def apicall(request):
    sensor_data = requests.get('https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH&results=20')
    sensor_data = sensor_data.json()['feeds']
    for s in sensor_data:
        date = s["created_at"].split("T")[0]
        time = s["created_at"].split("T")[1]
        time = time[:-1]

        timestamp = datetime.datetime.strptime(date + " "+time, "%Y-%m-%d %H:%M:%S")
        s["created_at"] = timestamp
    return JsonResponse(sensor_data, safe = False)

def analysis(request):
    return render(request, "incharge/analysis.html")


def success_submit(request):
    startDate = request.POST["startDate"]
    startTime = request.POST["startTime"]
    endTime = request.POST["endTime"]
    title = request.POST["title"]
    description = request.POST["description"]
    eventType = request.POST["eventType"]

    if startDate == "" or startTime == '' or endTime == '' or title == '' or description == '' or eventType == '':
        return render(request, 'incharge/schedule.html', {"error": "Please fill in all the fields."})
    else:
        eventType = int(eventType.lstrip('test'))
        data = m.Schedule(date=startDate, start_time=startTime, end_time=endTime,
                          title=title, description=description, event_type=eventType)
        lab = m.Lab.objects.get(id=request.session["lab_id"])
        added_by = m.User.objects.get(email=request.session["email"])
        data.lab = lab
        data.added_by = added_by
        data.save()
        return render(request, 'incharge/schedule.html', {"success": "Event added successfully!"})


def render_request(request):
    notif_data = m.Notification.objects.filter(
        category="2").order_by("-timestamp").all()
    user_id = m.User.objects.get(email=request.session["email"])
    requests = list()
    i = 0

    for n in notif_data:
        if n.data == None:
            continue

        date, start_time, end_time, uid = n.data.split(",")
        user = m.User.objects.get(id=n.Notification_to.id)
        name = user.fname + " " + user.lname

        start_timestamp = datetime.datetime.strptime(
            date + " "+start_time, "%d-%m-%Y %H:%M")
        end_timestamp = datetime.datetime.strptime(
            date + " "+end_time, "%d-%m-%Y %H:%M")

        requests.append({
            "id": n.id,
            "content": n.description,
            "at": n.timestamp,
            "date": start_timestamp.date(),
            "time": str(start_timestamp.strftime("%I:%M %p")) + " - "+str(end_timestamp.strftime("%I:%M %p")),
            "request_from": name
        })
    return render(request, "incharge/requests.html", {"requests": requests})


def accept_request(request, request_id):
    notif = m.Notification.objects.filter(id=request_id).update(category="3")
    notif = m.Notification.objects.get(id=request_id)
    desc = notif.description
    date, start_time, end_time, uid = notif.data.split(",")
    start_timestamp = datetime.datetime.strptime(
        date + " " + start_time, "%d-%m-%Y %H:%M")
    end_timestamp = datetime.datetime.strptime(
        date + " " + end_time, "%d-%m-%Y %H:%M")

    user = m.User.objects.get(email=request.session["email"])
    lab = m.Lab.objects.get(id=request.session["lab_id"])

    schedule_row = m.Schedule(date=start_timestamp.date(),
                              start_time=start_timestamp.time(),
                              end_time=end_timestamp.time(),
                              added_by=user,
                              lab=lab,
                              title="Request accepted",
                              description=desc,
                              event_type=0)
    schedule_row.save()
    return redirect("/incharge/requests")


def reject_request(request, request_id):
    notif = m.Notification.objects.filter(id=request_id).update(category="4")
    return redirect("/incharge/requests")
    pass
