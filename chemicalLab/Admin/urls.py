from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('table', views.table, name = 'table'),
    path('statistics', views.statistics, name = 'statistics'),
]