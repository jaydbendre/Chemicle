from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
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
    return render(request, 'incharge/schedule.html')

def analysis(request):
    return render(request , "incharge/analysis.html")

def success_submit(request):
    submit_data = request.POST
    start_date = request.POST['startDate']
    start_time = request.POST['startTime']
    end_time = request.POST['endTime']
    title = request.POST['title']
    description = request.POST['description']
    event_type = request.POST['eventType']

    if event_type == 'test1':
        event_type = 0
    elif event_type == 'test2':
        event_type = 1
    else:
        event_type = 2
    
    if start_date == '' or start_time == '' or  end_time == '' or title == '' or description == '' or event_type == '':
        pass

    else:
        user_data = m.User.objects.get(email = request.session['email'])
        lab_data = m.Lab.objects.get(id = request.session['lab_id'])
        data = m.Schedule.objects.create(date = start_date, start_time = start_time, end_time = end_time, title = title, description = description, event_type = event_type, lab = lab_data, added_by = user_data)
        data.save()
        # return HttpResponse(submit_data.items())
        return redirect('/incharge/schedule')
