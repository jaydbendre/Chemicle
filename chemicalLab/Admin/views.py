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
        if(user == 'user'):
            return redirect('/admin/table/users')
        if(lab == 'lab'):
            pass
        if(department == 'department'):
            pass
        if(role == 'role'):
            pass
    return render(request,"admin/table.html")  
    
def statistics(request):

    return render(request,"admin/statistics.html")

def t_users(request):
    if request.method == 'POST':
        u_id = request.POST.get("id")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        address = request.POST.get("address")
        role_id = request.POST.get("role_id")
        lab_id = request.POST.get("lab_id")
        print(u_id,fname,lname,email,address,role_id,lab_id)
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