from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('table', views.table, name = 'table'),
    path('table/users', views.t_users, name = 't_users'),
    path('statistics', views.statistics, name = 'statistics'),
]