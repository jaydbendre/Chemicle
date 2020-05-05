from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models as m
from django.contrib.auth import logout
import requests
import json
import datetime
import random
from chemicalLab.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

"""
To render the pages
"""


def index(request):
    return render(request, "landingpage/landingpage.html")


def render_login(request):
    del request.user
    del request.session
    return render(request, "login/login.html", {"error": ""})


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
    return render(request, "lab_operator/analysis.html", {"temperature": temperature, "lab_labels": lab_labels, "lab_data": lab_data, "humidity": humidity, "aqi": aqi, "created_at": created_at,
                                                          "temp_table": temp_table,
                                                          "hum_table": hum_table,
                                                          "aqi_table": aqi_table,
                                                          "temp_avg": temp_avg,
                                                          "hum_avg": humidity_avg,
                                                          "aqi_avg": aqi_avg,
                                                          "user_number": user_number
                                                          })


def schedule(request):
    return render(request, "lab_operator/schedule.html")


def notifications(request):
    user = m.User.objects.get(email=request.session["email"])
    notification_content = m.Notification.objects.all().filter(Notification_to=user)

    notif_data = dict()
    s_count = 0
    w_count = 0
    request_sent_count = 0
    request_accepted_count = 0
    request_rejected_count = 0
    for n in notification_content:
        # print(n.__dict__.items())

        if n.category not in notif_data.keys():
            notif_data[n.category] = dict()

        if n.category == "0":
            if n.data == None:
                continue
            schedule_info = m.Schedule.objects.get(id=int(n.data))
            notif_data[n.category][n.id] = {
                "content": n.description,
                "at": n.timestamp,
                "start_time": schedule_info.start_time,
                "end_time": schedule_info.end_time,
                "date": schedule_info.date,
                "event_description": schedule_info.description,
                "event_title": schedule_info.title,
                "viewed": n.delete_field
            }
            s_count += 1

        elif n.category == "1":
            if n.data == None:
                continue
            # print(n)
            d1, d2 = n.data.split(",")

            d1_class = "danger"
            d2_class = "danger"
            if d1 >= d2:
                d1_class = "success"
            else:
                d2_class = "success"

            notif_data[n.category][n.id] = {
                "content": n.description,
                "at": n.timestamp,
                "data_before": d1,
                "data_after": d2,
                "data_before_class": d1_class,
                "data_after_class": d2_class
            }
            w_count += 1
        elif n.category == "2":
            """
            Request sent
            """
            print("Hi")
            if n.data == None:
                continue
            date,start_time,end_time,uid = n.data.split(",")
            user = m.User.objects.get(id = uid)
            request_to = user.fname + " "+user.lname
            notif_data[n.category][n.id] = {
                "content": n.description,
                "at" : n.timestamp,
                "session_at": "On " + date + " from "+ start_time + " - "+end_time,
                "date": date,
                "start_time" : start_time,
                "end_time": end_time,
                "request_to" : request_to
            }
            request_sent_count += 1
            pass
        elif n.category == "3":
            """
            Request accepted
            """
            if n.data == None:
                continue
            date,start_time,end_time,uid = n.data.split(",")
            user = m.User.objects.get(id = uid)
            request_to = user.fname + " "+user.lname
            notif_data[n.category][n.id] = {
                "content": n.description,
                "at" : n.timestamp,
                "session_at": "On " + date + " from "+ start_time + " - "+end_time,
                "date": date,
                "start_time" : start_time,
                "end_time": end_time,
                "request_to" : request_to
            }
            request_accepted_count += 1
            pass
        elif n.category == "4":
            """
            Request rejected
            """
            if n.data == None:
                continue
            date,start_time,end_time,uid = n.data.split(",")
            user = m.User.objects.get(id = uid)
            request_to = user.fname + " "+user.lname
            notif_data[n.category][n.id] = {
                "content": n.description,
                "at" : n.timestamp,
                "session_at": "On " + date + " from "+ start_time + " - "+end_time,
                "date": date,
                "start_time" : start_time,
                "end_time": end_time,
                "request_to" : request_to
            }
            request_rejected_count += 1
            pass

    notif_data["unread_schedule"] = s_count
    notif_data["unread_warning"] = w_count
    notif_data["unread_r_sent"] = request_sent_count
    notif_data["unread_r_accept"] = request_accepted_count
    notif_data["unread_r_reject"] = request_rejected_count
    
    # print(notif_data.items())
    return render(request, "lab_operator/notifications.html", {"notif_data": notif_data})


"""
To check for something in the database
"""


def login(request):
    if request.user.is_authenticated:
        print(request.user.username)
        try:
            user_data = m.User.objects.get(email=str(request.user.email))
        except m.User.DoesNotExist:
            logout(request)
            # user_data = m.User.objects.get(email = "2017.jay.bendre@ves.ac.in")
            return render(request, "login/login.html", {"error": "User not found"})

        user_data = user_data.__dict__
        del user_data["_state"]
        print(user_data.items())

        # return HttpResponse(user_data.items())
        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"] + \
            " " + user_data["lname"]
        if user_data["role_id_id"] == 0:
            request.session["role"] = "Admin"
            return render(request, "admin/dashboard.html", {"user_data": user_data})
        elif user_data["role_id_id"] == 1:
            request.session["role"] = "Lab Incharge"
            return redirect('/incharge')
        else:
            request.session["role"] = "Lab Operator"
            # data = requests.get("https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH").text
            # return HttpResponse(data.items())
            return render(request, "lab_operator/dashboard.html", {"user_data": user_data})

    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if email != '' or password != '':
            try:
                user_data = m.User.objects.get(email=email, password=password)
            except m.User.DoesNotExist:
                return render(request, "login/login.html", {"error": "Invalid Email or password"})
            print("Hi")
            user_data = user_data.__dict__
            del user_data["_state"]
            print(user_data.items())

            request.session["email"] = user_data["email"]
            request.session["username"] = user_data["fname"] + \
                " " + user_data["lname"]
            Lab = m.Lab.objects.get(id=user_data["lab_id_id"])

            request.session["lab_id"] = user_data["lab_id_id"]
            request.session["lab"] = Lab.name
            if user_data["role_id_id"] == 0:
                request.session["role"] = "Admin"
                return redirect('/admin')
                # return render(request,"admin/dashboard.html",{"user_data" : user_data})
            elif user_data["role_id_id"] == 1:
                request.session["role"] = "Lab Incharge"
                return redirect('/incharge')
            else:
                request.session["role"] = "Lab Operator"
                # data = requests.get("https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH").text
                # return HttpResponse(data.items())
                return render(request, "lab_operator/dashboard.html", {"user_data": user_data})

    elif request.session["email"] != None:
        # return HttpResponse(request.session.items())
        try:
            user_data = m.User.objects.get(email=str(request.session["email"]))
        except m.User.DoesNotExist:
            logout(request)
            # user_data = m.User.objects.get(email = "2017.jay.bendre@ves.ac.in")
            return render(request, "login/login.html", {"error": "User not found"})

        user_data = user_data.__dict__
        del user_data["_state"]
        print(user_data.items())

        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"] + \
            " " + user_data["lname"]
        Lab = m.Lab.objects.get(id=user_data["lab_id_id"])

        request.session["lab_id"] = user_data["lab_id_id"]
        request.session["lab"] = Lab.name
        request.session["email"] = user_data["email"]
        request.session["username"] = user_data["fname"] + \
            " " + user_data["lname"]
        if user_data["role_id_id"] == 0:
            request.session["role"] = "Admin"
            return render(request, "admin/dashboard.html", {"user_data": user_data})
        elif user_data["role_id_id"] == 1:
            request.session["role"] = "Lab Incharge"
            return redirect('/incharge')
        else:
            request.session["role"] = "Lab Operator"
            # data = requests.get("https://api.thingspeak.com/channels/1017900/feeds.json?api_key=CQ98H95JG2IBYHNH").text
            # return HttpResponse(data.items())
            return render(request, "lab_operator/dashboard.html", {"user_data": user_data})

    else:
        return render(request, "login/login.html", {"error": "There has been error in processing your request"})


def get_historic_data(request, id):
    sensor_data = m.Sensor_log.objects.all()
    data = []
    if id == 1:
        for o in sensor_data:
            data.append(
                {
                    "date": str(o.timestamp),
                    "value": o.temperature
                }
            )
    elif id == 2:
        for o in sensor_data:
            data.append(
                {
                    "date": str(o.timestamp),
                    "value": o.humidity
                }
            )
    elif id == 3:
        for o in sensor_data:
            data.append(
                {
                    "date": str(o.timestamp),
                    "value": o.air_quality
                }
            )

    return JsonResponse(data, safe=False)


@csrf_exempt
def get_schedule_details(request):
    date = request.POST["date"]
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    schedule_data = m.Schedule.objects.order_by("date").all()
    data = []
    flag = False
    for s in schedule_data:
        s_date = datetime.datetime.strptime(str(s.date), "%Y-%m-%d")
        if date == s_date:
            flag = True
            user_data = m.User.objects.get(id=s.added_by_id)
            data.append({
                "start_time": s.start_time,
                "end_time": s.end_time,
                "description": s.description,
                "lab_id": s.lab_id,
                "added_by": user_data.fname + " " + user_data.lname,
                "event_type": s.event_type,
                "title": s.title,
            })

    if flag:
        return JsonResponse(data, safe=False)

    return JsonResponse({"error": "No events found for the day"})


@csrf_exempt
def get_scheduled_data(request):
    start_date = request.POST["s_date"]
    end_date = request.POST["e_date"]
    start_time = request.POST["s_time"]
    end_time = request.POST["e_time"]
    schedule_data = []
    if start_date == "" and end_date == "" and start_time == "" and end_time == "":
        return JsonResponse({"Error": "Please select a date/s "}, safe=False)

    elif start_date != "" and end_date == "":
        print("1")
        s_timestamp = ""
        if start_time != "":
            s_timestamp = start_date + " " + start_time+":00"
        else:
            s_timestamp = start_date + " 00:00:00"
        s_timestamp = datetime.datetime.strptime(
            s_timestamp, "%Y-%m-%d %H:%M:%S")
        data = m.Schedule.objects.order_by("-date", "-start_time").all()

        for d in data:

            c_s_timestamp = datetime.datetime.strptime(
                str(d.date) + " "+str(d.start_time), "%Y-%m-%d %H:%M:%S")
            c_e_timestamp = datetime.datetime.strptime(
                str(d.date) + " "+str(d.end_time), "%Y-%m-%d %H:%M:%S")

            if s_timestamp.date() <= c_s_timestamp.date() and d.lab_id == request.session["lab_id"]:
                # print("hi")

                if start_time != "" and s_timestamp.date() == c_s_timestamp.date():
                    if s_timestamp.time() <= c_s_timestamp.time():
                        schedule_data.append({
                            "id": d.id,
                            "title": d.title,
                            "time-range": str(d.start_time) + " - "+str(d.end_time),
                            "date": d.date,
                            "description": d.description
                        })
                    else:
                        continue
                elif start_time == "" and s_timestamp.date() == c_s_timestamp.date():
                    schedule_data.append({
                        "id": d.id,
                        "title": d.title,
                        "time-range": str(d.start_time) + " - "+str(d.end_time),
                        "date": d.date,
                        "description": d.description
                    })
        # print(schedule_data)
        return JsonResponse({"data": schedule_data}, safe=False)
    elif end_date != "" and start_date == "":
        print("2")
        e_timestamp = ""
        if end_time != "":
            e_timestamp = end_date + " " + end_time+":00"
        else:
            e_timestamp = end_date + " 00:00:00"
        e_timestamp = datetime.datetime.strptime(
            e_timestamp, "%Y-%m-%d %H:%M:%S")
        data = m.Schedule.objects.order_by("-date", "-start_time").all()

        for d in data:

            c_s_timestamp = datetime.datetime.strptime(
                str(d.date) + " "+str(d.start_time), "%Y-%m-%d %H:%M:%S")
            c_e_timestamp = datetime.datetime.strptime(
                str(d.date) + " "+str(d.end_time), "%Y-%m-%d %H:%M:%S")
            print(c_s_timestamp)
            if e_timestamp.date() >= c_s_timestamp.date() and d.lab_id == request.session["lab_id"]:
                # print("hi")
                if end_time != "" and e_timestamp.date() == c_s_timestamp.date():
                    if e_timestamp.time() >= c_s_timestamp.time():
                        schedule_data.append({
                            "id": d.id,
                            "title": d.title,
                            "time-range": str(d.start_time) + " - "+str(d.end_time),
                            "date": d.date,
                            "description": d.description
                        })
                    else:
                        continue
                elif end_time == "" and e_timestamp.date() == c_s_timestamp.date():
                    schedule_data.append({
                        "id": d.id,
                        "title": d.title,
                        "time-range": str(d.start_time) + " - "+str(d.end_time),
                        "date": d.date,
                        "description": d.description
                    })

        # print(schedule_data)
        return JsonResponse({"data": schedule_data}, safe=False)
    else:
        print("3")
        s_timestamp = ""
        if start_time != "":
            s_timestamp = start_date + " " + start_time+":00"
        else:
            s_timestamp = start_date + " 00:00:00"
        s_timestamp = datetime.datetime.strptime(
            s_timestamp, "%Y-%m-%d %H:%M:%S")
        e_timestamp = ""
        if end_time != "":
            e_timestamp = end_date + " " + end_time+":00"
        else:
            e_timestamp = end_date + " 00:00:00"
        e_timestamp = datetime.datetime.strptime(
            e_timestamp, "%Y-%m-%d %H:%M:%S")
        data = m.Schedule.objects.order_by("-date", "-start_time").all()

        for d in data:

            c_s_timestamp = datetime.datetime.strptime(
                str(d.date) + " "+str(d.start_time), "%Y-%m-%d %H:%M:%S")
            c_e_timestamp = datetime.datetime.strptime(
                str(d.date) + " "+str(d.end_time), "%Y-%m-%d %H:%M:%S")

            if s_timestamp.date() <= c_s_timestamp.date() and e_timestamp.date() >= c_s_timestamp.date() and d.lab_id == request.session["lab_id"]:
                # print("hi")
                if s_timestamp.date() == c_s_timestamp.date():
                    if s_timestamp.time() <= c_s_timestamp.time() and e_timestamp.time() >= c_e_timestamp.time():
                        schedule_data.append({
                            "id": d.id,
                            "title": d.title,
                            "time-range": str(d.start_time) + " - "+str(d.end_time),
                            "date": d.date,
                            "description": d.description
                        })
                    else:
                        continue
                if e_timestamp.date() == c_s_timestamp.date():
                    if e_timestamp.time() <= c_e_timestamp.time() and e_timestamp.time() >= c_s_timestamp.time():
                        schedule_data.append({
                            "id": d.id,
                            "title": d.title,
                            "time-range": str(d.start_time) + " - "+str(d.end_time),
                            "date": d.date,
                            "description": d.description
                        })
                    else:
                        continue

        # print(schedule_data)
        return JsonResponse({"data": schedule_data}, safe=False)
        return JsonResponse(request.POST, safe=False)


@csrf_exempt
def get_sensor_data(request):
    id = request.POST["schedule_id"]

    schedule_info = m.Schedule.objects.get(id=id)
    schedule_info = schedule_info.__dict__
    s_timestamp = datetime.datetime.strptime(str(
        schedule_info["date"])+" " + str(schedule_info["start_time"]), "%Y-%m-%d %H:%M:%S")
    e_timestamp = datetime.datetime.strptime(str(
        schedule_info["date"])+" " + str(schedule_info["end_time"]), "%Y-%m-%d %H:%M:%S")
    sensor_data = m.Sensor_log.objects.filter(
        lab_id=request.session["lab_id"]).all()

    sensor_info = {
        "temp": [],
        "humidity": [],
        "aqi": [],
        "index": [],
        "temp_avg": 0,
        "hum_avg": 0,
        "aqi_avg": 0
    }

    i = 0
    print(s_timestamp, e_timestamp)
    for s in sensor_data:
        s = s.__dict__
        if s["timestamp"] >= s_timestamp and s["timestamp"] <= e_timestamp:
            i += 1
            sensor_info["index"].append(i)
            sensor_info["temp"].append(s["temperature"])
            sensor_info["humidity"].append(s["humidity"])
            sensor_info["aqi"].append(s["air_quality"])
            # print(sensor_data.items())

    if len(sensor_info["temp"]) == 0:
        return JsonResponse({"Error": "No data found"}, safe=False)
    sensor_info["temp_avg"] = "{:.2f}".format(sum(sensor_info["temp"])/i)
    sensor_info["hum_avg"] = "{:.2f}".format(sum(sensor_info["humidity"])/i)
    sensor_info["aqi_avg"] = "{:.2f}".format(sum(sensor_info["aqi"])/i)
    return JsonResponse(sensor_info)


@csrf_exempt
def create_notif_anamoly(request, id):
    if id == 1:
        temp1 = request.POST["temp_before"]
        temp2 = request.POST["temp_after"]

        description = ""
        if temp1 > temp2:
            description = "Warning , The temperature has dropped by " + \
                str(float(temp1)-float(temp2)) + " °C"
        else:
            description = "Warning , The temperature has spiked by " + \
                str(float(temp2)-float(temp1)) + " °C"

        user_data = m.User.objects.all().filter(
            lab_id=request.session["lab_id"])

        admin = m.User.objects.get(email="2017.jatin.acharya@ves.ac.in")
        for u in user_data:
            m.Notification.create_notification(
                to=u,
                by=admin,
                description=description,
                category=1
            )
        return JsonResponse({"Success": "Done"})
    elif id == 2:
        hum1 = request.POST["hum_before"]
        hum2 = request.POST["hum_after"]

        description = ""
        if hum1 > hum2:
            description = "Warning , The humidity has dropped by " + \
                str(float(hum1)-float(hum2)) + " %"
        else:
            description = "Warning , The humidity has spiked by " + \
                str(float(hum2)-float(hum1)) + " %"

        user_data = m.User.objects.all().filter(
            lab_id=request.session["lab_id"])

        admin = m.User.objects.get(email="2017.jatin.acharya@ves.ac.in")
        for u in user_data:
            m.Notification.create_notification(
                to=u,
                by=admin,
                description=description,
                category=1
            )
        return JsonResponse({"Success": "Done"})
    elif id == 3:
        aqi1 = request.POST["aqi_before"]
        aqi2 = request.POST["aqi_after"]

        description = ""
        if aqi1 > aqi2:
            description = "Warning , The Air Quality has dropped by " + \
                str(float(aqi1)-float(aqi2))
        else:
            description = "Warning , The Air Quality has spiked by " + \
                str(float(aqi2)-float(aqi1))

        user_data = m.User.objects.all().filter(
            lab_id=request.session["lab_id"])

        admin = m.User.objects.get(email="2017.jatin.acharya@ves.ac.in")
        for u in user_data:
            m.Notification.create_notification(
                to=u,
                by=admin,
                description=description,
                category=1
            )
        return JsonResponse({"Success": "Done"})
    else:
        return JsonResponse({"Error": "Invalid URL"})
    pass


@csrf_exempt
def get_all_notifs(request):
    user_id = m.User.objects.get(email=request.session["email"])
    user_notifications = m.Notification.objects.all().filter(Notification_to=user_id.id)
    notif = []
    i = 0
    for u in user_notifications:
        u = u.__dict__
        by = m.User.objects.get(id=u["Notification_by_id"])
        notif.append({
            "by": by.fname + " " + by.lname,
            "category": u["category"],
            "at": u["timestamp"],
            "viewed": u["delete_field"],
            "description": u["description"],
        })

    return JsonResponse({"Notif": notif})


def log_out(request):
    logout(request)
    return redirect("/")

# Email


def email(request):
    data = m.User.objects.get(id=10001)
    data = data.__dict__
    recepient = data["email"]

    subject = 'Test'
    message = 'test2'
    send_mail(subject, message, EMAIL_HOST_USER,
              [recepient], fail_silently=False)
    return HttpResponse('done')
