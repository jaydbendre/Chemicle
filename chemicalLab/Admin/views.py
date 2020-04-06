from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models as m

# Create your views here.
def index(request):
    return render(request, "admin/boilerplate.html")

def dashboard(request):
    # email = "2017.jatin.acharya@ves.ac.in"
    # password="test"
    # user_data = m.User.objects.get(email = email ,password = password)
    # user_data=user_data.__dict__
    # return HttpResponse(user_data.values())
    number_lab_operator = m.User.objects.filter(role_id = 2).all()
    number_lab_incharge = m.User.objects.filter(role_id = 1).all()
    user_data={
        "lab_operator" : len(number_lab_operator),
        "lab_incharge" : len(number_lab_incharge),
    }
    # return HttpResponse(len(number_lab_operator))
    return render(request, "admin/dashboard.html",user_data)

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
    
def statistics(request):

    return render(request,"admin/statistics.html")

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
    schedule_data = m.Schedule.objects.values_list()
    schedule_content = dict()
    for schedule in schedule_data:
        schedule_content[str(schedule[0])] = {
            "id" : schedule[0],
            "date" : schedule[1],
            "start_time" : schedule[2],
            "end_time" : schedule[3],
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
    return HttpResponse("table/requests")