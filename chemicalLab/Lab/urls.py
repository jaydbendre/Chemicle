from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/',views.render_login , name = "render_login"),
    path('auth_user/',views.login, name = "login"),
    path("logout/",views.log_out , name = "logout")
    # path('test/', views.send_data, name = 'test')
]