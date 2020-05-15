from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Lab import models as m
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from .models import FileLog
import datetime
import requests
import pandas as pd
import numpy as np
from django.core.files.storage import FileSystemStorage
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

def incharge_profile(request):
    if request.method == "POST":
        u_id = request.POST.get("id")
        fname = request.POST.get("firstName")
        lname = request.POST.get("lastName")
        email = request.POST.get("email")
        address = request.POST.get("address")
        print(u_id,fname,lname,email,address)
        update_user = m.User.objects.get(id = u_id)
        update_user.fname = fname
        update_user.lname = lname
        update_user.email = email
        update_user.address = address
        update_user.save(update_fields=['fname','lname','email','address'])
    user_data = m.User.objects.get(email = request.session["email"])
    user_data = user_data.__dict__

    return render(request, "incharge/profile.html",{"user_data":user_data})

@csrf_exempt
def apicall(request):
    sensor_data = requests.get(
        'https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH&results=20')
    sensor_data = sensor_data.json()['feeds']
    for s in sensor_data:
        date = s["created_at"].split("T")[0]
        time = s["created_at"].split("T")[1]
        time = time[:-1]

        timestamp = datetime.datetime.strptime(
            date + " "+time, "%Y-%m-%d %H:%M:%S")
        s["date"] = str(timestamp)
    return JsonResponse(sensor_data, safe=False)


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
            lab_count[o.lab_id.id] += 1
        temperature.append(
            o.temperature
        )

        created_at.append(datetime.datetime.strftime(
            o.timestamp, "%d %B, %Y %I:%M %p"))
        humidity.append(o.humidity)
        aqi.append(o.air_quality)

    temp_avg = sum(temperature)/len(temperature)
    humidity_avg = sum(humidity)/len(humidity)
    aqi_avg = sum(aqi)/len(aqi)

    temperature = temperature[:20]
    aqi = aqi[:20]
    humidity = humidity[:20]

    lab_labels = [v for v in lab_count.keys()]
    lab_data = []

    temp_table = zip(temperature, created_at)
    hum_table = zip(humidity, created_at)
    aqi_table = zip(aqi, created_at)

    for k, v in lab_count.items():
        lab_data.append(
            {
                "Lab": k,
                "Count": v
            }
        )
    return render(request, "incharge/analysis.html", {"temperature": temperature, "lab_labels": lab_labels, "lab_data": lab_data, "humidity": humidity, "aqi": aqi, "created_at": created_at,
                                                      "temp_table": temp_table,
                                                      "hum_table": hum_table,
                                                      "aqi_table": aqi_table,
                                                      "temp_avg": temp_avg,
                                                      "hum_avg": humidity_avg,
                                                      "aqi_avg": aqi_avg,
                                                      "user_number": user_number
                                                      })


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


lm = LinearRegression()
scaler = MinMaxScaler()


def upload_file(request):

    uid = m.User.objects.get(email=request.session["email"])
    folder = '../uploads/{}/'.format(uid.id)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location=folder)
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)

        df = pd.DataFrame(pd.read_csv("{}/{}".format(folder, filename)))

        independent_var = ""
        dependent_var = request.POST["dependent_variable"]
        if request.POST["independent_variable"] != "":
            if "," not in request.POST["independent_variable"]:
                independent_var = [request.POST["independent_variable"]]
            else:
                independent_var = request.POST["independent_variable"].split(
                    ",")
        else:
            independent_var = list(df.drop(dependent_var).columns)

        X = np.array(df[independent_var]).reshape(-1, 1)
        y = np.array(df[dependent_var]).reshape(-1, 1)

        scaler.fit(X)

        X = scaler.transform(X)
        y = scaler.transform(y)

        split = float(request.POST["ratio"])
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=split, random_state=42)

        model = lm.fit(X_train, y_train)
        pred = lm.predict(X_test)
        predictions = list(pred)
        score = float(lm.score(X_test, y_test))
        coef = float(lm.coef_)

        mean_error = float(mean_squared_error(y_test, pred))

        x = list()
        y = list()
        pred = list()

        for var in X_test:
            x.append(float(var[0]))
        for var in y_test:
            y.append(float(var[0]))
        for var in predictions:
            pred.append(float(var[0]))

        print(independent_var[0])
        data = {
            "x": list(x),
            "y": list(y),
            "pred": list(pred),
            "score": "{:.4f}".format(score),
            "coef": "{:.4f}".format(coef),
            "dependent_var": dependent_var.capitalize(),
            "independent_var": independent_var[0].capitalize(),
            "mean_squared_error": "{:.4f}".format(mean_error)
        }
        return JsonResponse(
            data, safe=False
        )
    else:
        return HttpResponse("No File")


@csrf_exempt
def predict_single_val(request):
    global lm, scaler

    data = np.array(float(request.POST["dependent_value"])).reshape(-1, 1)
    data = scaler.transform(data)
    predicted_val = lm.predict(data)
    predicted_val = float(scaler.inverse_transform(predicted_val))
    return JsonResponse({"Prediction": "{:.4f}".format(predicted_val)})

@csrf_exempt
def gen_schedule(request):
    start_date = request.POST['date_input']+ ' 00:00:00'
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S") 
    end_date = start_date + datetime.timedelta(days = 6)
    
    data = dict()
    
    for i in range(0,7):
        data[str( (start_date + datetime.timedelta(days = i)).date() )] = list()
    
    lab = m.Lab.objects.get(id = request.session["lab_id"])
    
    start_time = list()
    end_time = list()
    new_date = datetime.datetime.strptime(str(start_date.date())+" 08:00:00","%Y-%m-%d %H:%M:%S")
    for i in range(5):
        start_time.append(new_date)
        new_date = new_date + datetime.timedelta(hours = 2)
        end_time.append(new_date)

    print(start_time, end_time)
    for i in data.keys():
        schedule_data = m.Schedule.objects.order_by('start_time').filter(date = i, lab= lab).all()
        for s in schedule_data:

            start_timestamp = datetime.datetime.strptime(str(s.date) + " "+ str(s.start_time) ,"%Y-%m-%d %H:%M:%S" )
            end_timestamp = datetime.datetime.strptime(str(s.date) + " "+ str(s.end_time) ,"%Y-%m-%d %H:%M:%S" )
            
            j=0
            flag = 9999
            for start,end in zip(start_time,end_time):
                if start_timestamp.time() >= start.time() and end_timestamp.time() <=end.time():
                    flag= j
                    break
                j+=1
            data[i].append({
                'start_time' : s.start_time,
                'end_time' : s.end_time,
                'lab' : s.lab.id,
                'title' : s.title,
                'event_type' : s.event_type,
                "row_id": flag
            })
    
    return JsonResponse(data, safe = False)