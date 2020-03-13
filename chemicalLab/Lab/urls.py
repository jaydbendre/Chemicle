from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('test/', views.send_data, name = 'test')
]