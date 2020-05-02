from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models as m
import datetime

# Create your views here.
def index(request):
    return render(request, "admin/boilerplate.html")

def dashboard(request):
    # email = "2017.jatin.acharya@ves.ac.in"
    # password="test"
    # user_data = m.User.objects.get(email = email ,password = password)
    # user_data=user_data.__dict__
    # return HttpResponse(user_data.values())
    sensor_log = m.Sensor_log.objects.order_by("-timestamp").all()

    temperature = []
    humidity = []
    aqi = [] 

    for i in sensor_log:
        temperature.append(i.temperature)
        humidity.append(i.humidity)
        aqi.append(i.air_quality)
    
    temp_avg = sum(temperature)/len(temperature)
    hum_avg = sum(humidity)/len(humidity)
    aqi_avg = sum(aqi)/len(aqi)

    print(temp_avg,hum_avg,aqi_avg)

    number_lab_operator = m.User.objects.filter(role_id = 2).all()
    number_lab_incharge = m.User.objects.filter(role_id = 1).all()
    number_departments = m.Department.objects.all().count()
    data={
        "lab_operator" : len(number_lab_operator),
        "lab_incharge" : len(number_lab_incharge),
        "department": number_departments,
        "temp_avg": temp_avg,
        "hum_avg": hum_avg,
        "aqi_avg": aqi_avg,
    }
    # return HttpResponse(len(number_lab_operator))
    return render(request, "admin/dashboard.html",data)

def table(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        lab = request.POST.get("lab")
        department = request.POST.get("department")
        role = request.POST.get("role")
        schedule = request.POST.get("schedule")
        request = request.POST.get("request")
        if(user == 'user'):
            return redirect('/admin/table/users')
        if(lab == 'lab'):
            return redirect('/admin/table/labs')
        if(department == 'department'):
            return redirect('/admin/table/departments')
        if(role == 'role'):
            return redirect('/admin/table/roles')
        if(schedule == 'schedule'):
            return redirect('/admin/table/schedules')
        if(request == 'request'):
            return redirect('/admin/table/requests')
    return render(request,"admin/table.html")  
    

def t_users(request):
    if request.method == 'POST':
        # dummy = request.POST.get("dummy")
        if request.POST : 
            if '_save' in request.POST:
                u_id = request.POST.get("u_id")
                fname = request.POST.get("fname")
                lname = request.POST.get("lname")
                email = request.POST.get("email")
                address = request.POST.get("address")
                role_id = request.POST.get("role_id")
                lab_id = request.POST.get("lab_id")
                print(u_id,fname,lname,email,address,role_id,lab_id)
                update_user = m.User.objects.get(id=u_id)
                update_user.id = u_id
                update_user.fname = fname
                update_user.lname = lname
                update_user.email = email
                update_user.address = address
                update_user.role_id_id = int(role_id)
                update_user.lab_id_id = int(lab_id)
                update_user.save()
            if '_delete' in request.POST:
                u_id = request.POST.get("u_id")
                delete_user = m.User.objects.get(id=u_id)
                delete_user.delete()
        
        # user_data = m.User.objects.get(id=user_id)
        # print(user_data)
    user_data = m.User.objects.values_list()
    user_content = dict()
    for user in user_data:
        user_content[str(user[0])] = {
            "id" : user[0],
            "fname" : user[1],
            "lname" : user[2],
            "email" : user[3],
            "address" : user[5],
            "role_id" : user[6],
            "lab_id" : user[7]
        }
    data = {
        'user_data':user_content
    }
    return render(request, "admin/tables/user.html",{"data":data})

def t_labs(request):
    if request.method == 'POST':
        if request.POST : 
            if '_save' in request.POST:
                lab_id = request.POST.get("lab_id")
                name = request.POST.get("name")
                dept_id = request.POST.get("dept_id")
                print(lab_id,name,dept_id)
                update_lab = m.Lab.objects.get(id=lab_id)
                update_lab.id = lab_id
                update_lab.name = name
                update_lab.dept_id_id = dept_id
                update_lab.save()
            if '_delete' in request.POST:
                lab_id = request.POST.get("lab_id")
                delete_lab = m.Lab.objects.get(id=lab_id)
                delete_lab.delete()
    lab_data = m.Lab.objects.values_list()
    lab_content = dict()
    for lab in lab_data:
        lab_content[str(lab[0])] = {
            "id" : lab[0],
            "name" : lab[1],
            "dept_id": lab[2]
        }
    data = {
        "lab_data" : lab_content
    }
    return render(request, "admin/tables/lab.html",{"data":data})


def t_departments(request):
    if request.method == 'POST':
        if request.POST : 
            if '_save' in request.POST:
                dept_id = request.POST.get("dept_id")
                name = request.POST.get("name")
                print(dept_id,name)
                update_dept = m.Department.objects.get(id=dept_id)
                update_dept.id = dept_id
                update_dept.name = name
                update_dept.save()
            if '_delete' in request.POST:
                dept_id = request.POST.get("dept_id")
                delete_dept = m.Lab.objects.get(id=dept_id)
                delete_dept.delete()
    dept_data = m.Department.objects.values_list()
    dept_content = dict()
    for dept in dept_data:
        dept_content[str(dept[0])] = {
            "id" : dept[0],
            "name" : dept[1]
        }
    data = {
        "dept_data" : dept_content
    }
    return render(request, "admin/tables/department.html",{"data":data})

def t_roles(request):
    if request.method == 'POST':
        if request.POST : 
            if '_save' in request.POST:
                role_id = request.POST.get("role_id")
                post = request.POST.get("post")
                print(role_id,post)
                update_role = m.Role.objects.get(id=role_id)
                update_role.id = role_id
                update_role.post = post
                update_role.save()
            if '_delete' in request.POST:
                role_id = request.POST.get("role_id")
                delete_role = m.Lab.objects.get(id=role_id)
                delete_role.delete()
    role_data = m.Role.objects.values_list()
    role_content = dict()
    for role in role_data:
        role_content[str(role[0])] = {
            "id" : role[0],
            "post" : role[1]
        }
    data = {
        "role_data" : role_content
    }
    return render(request, "admin/tables/role.html",{"data":data})
    

def t_schedules(request):
    if request.method == 'POST':
        if request.POST : 
            if '_save' in request.POST:
                schedule_id = request.POST.get("schedule_id")
                date = request.POST.get("date")
                start_time = request.POST.get("start_time")
                end_time = request.POST.get("end_time")
                lab = request.POST.get("lab")
                added_by = request.POST.get("added_by")
                description = request.POST.get("description")
                event_type = request.POST.get("event_type")
                title = request.POST.get("title")
                print(schedule_id,date,start_time,end_time,lab,added_by,description,event_type,title)
                update_schedule = m.Schedule.objects.get(id=schedule_id)
                update_schedule.id = schedule_id
                update_schedule.date = date
                update_schedule.start_time = start_time
                update_schedule.end_time = end_time
                update_schedule.lab_id = lab
                update_schedule.added_by_id = added_by
                update_schedule.description = description
                update_schedule.event_type = event_type
                update_schedule.title = title
                update_schedule.save()
            if '_delete' in request.POST:
                schedule_id = request.POST.get("schedule_id")
                delete_schedule = m.Lab.objects.get(id=schedule_id)
                delete_schedule.delete()
    schedule_data = m.Schedule.objects.values_list()
    schedule_content = dict()
    for schedule in schedule_data:
        schedule_content[str(schedule[0])] = {
            "id" : schedule[0],
            "date" : str(schedule[1]),
            "start_time" : str(schedule[2]),
            "end_time" : str(schedule[3]),
            "lab" : schedule[4],
            "added_by" : schedule[5],
            "description" : schedule[6],
            "event_type" : schedule[7],
            "title" : schedule[8]
        }
    data = {
        "schedule_data" : schedule_content
    }
    return render(request, "admin/tables/schedule.html",{"data":data})
    

def t_requests(request):
    if request.method == 'POST':
        if request.POST : 
            if '_save' in request.POST:
                req_id = request.POST.get("req_id")
                description = request.POST.get("description")
                req_from = request.POST.get("req_from")
                req_to = request.POST.get("req_to")
                humidity = request.POST.get("humidity")
                temperature = request.POST.get("temperature")
                print(req_id,description,req_from,req_to,humidity,temperature)
                update_request = m.Request.objects.get(id=req_id)
                update_request.id = req_id
                update_request.description = description
                update_request.req_from_id = req_from
                update_request.req_to = req_to
                update_request.humidity = humidity
                update_request.temperature = temperature
                update_request.save()
            if '_delete' in request.POST:
                req_id = request.POST.get("req_id")
                delete_request = m.Lab.objects.get(id=req_id)
                delete_request.delete()
    request_data = m.Request.objects.values_list()
    request_content = dict()
    print(request_data)
    for req in request_data:
        request_content[str(req[0])] = {
            "id" : req[0],
            "description" : req[1],
            "request_from" : req[2],
            "request_to" :  req[3],
            "humidity" : req[4],
            "temperature" : req[5],
        }
    data = {
        "request_data" : request_content
    }
    return render(request, "admin/tables/request.html",{"data":data})
    
def statistics(request):
    if request.method == 'POST':
        lab1001 = request.POST.get("lab1001")
        lab1004 = request.POST.get("lab1004")
        compare = request.POST.get("compare")
        if(lab1001 == 'lab1001'):
            return redirect('/admin/statistics/lab1001')
        if(lab1004 == 'lab1004'):
            return redirect('/admin/statistics/lab1004')
        if(compare == 'compare'):
            return redirect('/admin/statistics/compare')
    return render(request,"admin/statistics.html")

def lab1001(request):
    sensor_data = m.Sensor_log.objects.order_by("-timestamp").all()
    
    temperature = []
    created_at = []
    humidity = []
    aqi = []

    for i in sensor_data:
        if(i.lab_id.id == 1001):
            temperature.append(i.temperature)
            created_at.append(datetime.datetime.strftime(i.timestamp, "%d %B, %Y %I:%M %p"))
            humidity.append(i.humidity)
            aqi.append(i.air_quality)
    
    temp_avg = sum(temperature)/len(temperature)
    hum_avg = sum(humidity)/len(humidity)
    aqi_avg = sum(aqi)/len(aqi)
    
    temperature = temperature[:20]
    created_at = created_at[:20]
    humidity = humidity[:20]
    aqi = aqi[:20]

    temp_table = zip(temperature, created_at)
    hum_table = zip(humidity, created_at)
    aqi_table = zip(aqi, created_at)

    user_number = m.User.objects.filter(lab_id=1001).all()
    user_number = len(user_number)

    return render(request,"admin/statistics/charts/1001/analysisPage.html", { "temperature": temperature, "created_at": created_at, "humidity": humidity, "aqi": aqi, "temp_avg": temp_avg,
    "hum_avg":hum_avg, "aqi_avg":aqi_avg, "temp_table":temp_table, "hum_table":hum_table, "aqi_table":aqi_table, "user_number": user_number })
        # return HttpResponse(o)
        # if o.lab_id.id not in lab_count.keys():
        #     lab_count[o.lab_id.id] = 1
        # else:
        #     lab_count[o.lab_id.id] += 1

    # print(lab_count)
    # return HttpResponse(sensor_data)

def lab1004(request):
    sensor_data = m.Sensor_log.objects.order_by("-timestamp").all()
    
    temperature = []
    created_at = []
    humidity = []
    aqi = []

    for i in sensor_data:
        if(i.lab_id.id == 1004):
            temperature.append(i.temperature)
            created_at.append(datetime.datetime.strftime(i.timestamp, "%d %B, %Y %I:%M %p"))
            humidity.append(i.humidity)
            aqi.append(i.air_quality)
    
    temp_avg = sum(temperature)/len(temperature)
    hum_avg = sum(humidity)/len(humidity)
    aqi_avg = sum(aqi)/len(aqi)
    
    temperature = temperature[:20]
    created_at = created_at[:20]
    humidity = humidity[:20]
    aqi = aqi[:20]

    temp_table = zip(temperature, created_at)
    hum_table = zip(humidity, created_at)
    aqi_table = zip(aqi, created_at)

    user_number = m.User.objects.filter(lab_id=1004).all()
    user_number = len(user_number)

    return render(request,"admin/statistics/charts/1004/analysisPage.html", { "temperature": temperature, "created_at": created_at, "humidity": humidity, "aqi": aqi, "temp_avg": temp_avg,
    "hum_avg":hum_avg, "aqi_avg":aqi_avg, "temp_table":temp_table, "hum_table":hum_table, "aqi_table":aqi_table, "user_number": user_number })
        # return HttpResponse(o)
    return HttpResponse("lab1004")

def compare(request):
    sensor_data = m.Sensor_log.objects.order_by("-timestamp").all()

    temperature1 = []
    created_at1 = []
    humidity1 = []
    aqi1 = []

    temperature4 = []
    created_at4 = []
    humidity4 = []
    aqi4 = []

    for i in sensor_data:
        if(i.lab_id.id == 1001):
            temperature1.append(i.temperature)
            created_at1.append(datetime.datetime.strftime(i.timestamp, "%d %B, %Y %I:%M %p"))
            humidity1.append(i.humidity)
            aqi1.append(i.air_quality)
        elif(i.lab_id.id == 1004):
            temperature4.append(i.temperature)
            created_at4.append(datetime.datetime.strftime(i.timestamp, "%d %B, %Y %I:%M %p"))
            humidity4.append(i.humidity)
            aqi4.append(i.air_quality)

    temp_avg1 = sum(temperature1)/len(temperature1)
    hum_avg1 = sum(humidity1)/len(humidity1)
    aqi_avg1 = sum(aqi1)/len(aqi1)

    temp_avg4 = sum(temperature4)/len(temperature4)
    hum_avg4 = sum(humidity4)/len(humidity4)
    aqi_avg4 = sum(aqi4)/len(aqi4)

    temperature1 = temperature1[:20]
    created_at1 = created_at1[:20]
    humidity1 = humidity1[:20]
    aqi1 = aqi1[:20]

    temperature4 = temperature4[:20]
    created_at4 = created_at4[:20]
    humidity4 = humidity4[:20]
    aqi4 = aqi4[:20]

    temp_table1 = zip(temperature1, created_at1)
    hum_table1 = zip(humidity1, created_at1)
    aqi_table1 = zip(aqi1, created_at1)

    temp_table4 = zip(temperature4, created_at4)
    hum_table4 = zip(humidity4, created_at4)
    aqi_table4 = zip(aqi4, created_at4)

    user_number1 = m.User.objects.filter(lab_id=1001).all()
    user_number1 = len(user_number1)

    user_number4 = m.User.objects.filter(lab_id=1004).all()
    user_number4 = len(user_number4)

    return render(request,"admin/statistics/charts/compare/analysisPage.html", { "temperature1": temperature1, "created_at1": created_at1, "humidity1": humidity1, "aqi1": aqi1, "temp_avg1": temp_avg1,
    "hum_avg1":hum_avg1, "aqi_avg1":aqi_avg1, "temp_table1":temp_table1, "hum_table1":hum_table1, "aqi_table1":aqi_table1, "user_number1": user_number1,
    "temperature4": temperature4, "created_at4": created_at4, "humidity4": humidity4, "aqi4": aqi4, "temp_avg4": temp_avg4,
    "hum_avg4":hum_avg4, "aqi_avg4":aqi_avg4, "temp_table4":temp_table4, "hum_table4":hum_table4, "aqi_table4":aqi_table4, "user_number4": user_number4 })