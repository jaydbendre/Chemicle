from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return HttpResponse('hi')

def render_login(request):
    return render(request,"login.html")