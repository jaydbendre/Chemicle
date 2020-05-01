from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('table', views.table, name = 'table'),
    path('table/users', views.t_users, name = 't_users'),
    path('table/labs', views.t_labs, name = 't_labs'),
    path('table/departments', views.t_departments, name = 't_departments'),
    path('table/roles', views.t_roles, name = 't_roles'),
    path('table/schedules', views.t_schedules, name = 't_schedules'),
    path('table/requests', views.t_requests, name = 't_requests'),
    path('statistics', views.statistics, name = 'statistics'),
    path('statistics/lab1001', views.lab1001 , name = 'lab1001'),
    path('statistics/lab1004', views.lab1004, name = 'lab1004'),
    path('statistics/compare', views.compare, name = 'compare'),
]