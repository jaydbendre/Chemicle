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

    return render(request,"admin/table.html")
    
def statistics(request):

    return render(request,"admin/statistics.html")