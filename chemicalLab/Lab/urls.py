from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/',views.render_login , name = "render_login"),
    path('auth_user/',views.login, name = "login"),
    path("logout/",views.log_out , name = "logout"),
    path("analysis/" ,views.analysis , name="analysis"),
    path("view_schedule/" ,views.schedule , name = "view_schedule")
]