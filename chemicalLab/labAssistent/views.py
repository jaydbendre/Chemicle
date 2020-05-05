from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Lab import models as m
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
    return render(request, 'incharge/schedule.html', {"error":'' ,"success":""})


def analysis(request):
    return render(request, "incharge/analysis.html")

def success_submit(request):
    startDate = request.POST["startDate"]
    startTime = request.POST["startTime"]
    endTime = request.POST["endTime"]
    title = request.POST["title"]
    description = request.POST["description"]
    eventType = request.POST["eventType"]

    if startDate == "" or startTime == '' or endTime == '' or  title == '' or description == '' or eventType == '':
        return render (request, 'incharge/schedule.html',{"error":"Please fill in all the fields."})
    else:
        eventType = int(eventType.lstrip('test'))
        data = m.Schedule(date = startDate, start_time = startTime, end_time = endTime, title = title, description = description, event_type = eventType)
        lab = m.Lab.objects.get(id = request.session["lab_id"])
        added_by = m.User.objects.get(email = request.session["email"])
        data.lab = lab
        data.added_by = added_by
        data.save()
        return render(request, 'incharge/schedule.html', {"success":"Event added successfully!"})
