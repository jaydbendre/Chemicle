from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/',views.render_login , name = "render_login"),
    path('test/', views.send_data, name = 'test')
]