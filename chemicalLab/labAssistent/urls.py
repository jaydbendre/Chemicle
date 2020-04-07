from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name='incharge_dashboard'),
    path("schedule", views.schedule, name='incharge_schedule'),
]
