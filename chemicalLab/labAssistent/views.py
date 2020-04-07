from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'incharge/dashboard.html')


def schedule(request):
    return render(request, 'incharge/schedule.html')
