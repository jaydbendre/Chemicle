from django.urls import path
from . import views

"""
Important things in urls.py

a. Map an exisiting views function to the path which means 
    127.0.0.1:8000/incharge/ access dashboard() in views
    127.0.0.1:8000/incharge/schedule access schedule() in views

b.To send data via a URL aka URL parameter
    path("path_name/<datatype:var_name>" , views.get_function(),name = "some_test_URL"),
    
    and in views.py :
    def function_name(request,var_name):
    
    should be the function definition
    
    Example of a path:
    path("get_user_details/<int:id>",views.get_user_details , name = "get_user_details")
    
    and views function :
    def get_user_details(request,id):
    
    to see how to actually pass content in the URL see the documentation in incharge/boilerplate.html
"""


urlpatterns = [
    path("", views.dashboard, name='incharge_dashboard'),
    path("schedule", views.schedule, name='incharge_schedule'),
    path("analysis", views.analysis, name="incharge_analysis"),
    path("success_submit", views.success_submit, name='success_submit'),
    path("requests", views.render_request, name="request"),
    path("accept_request/<int:request_id>",
         views.accept_request, name="accept_request"),
    path("reject_request/<int:request_id>",
         views.reject_request, name="accept_request"),
    path("sensor_data_20", views.apicall, name="sensor_data_20"),
    path("upload_file", views.upload_file, name="upload_file"),
    path("predict", views.predict_single_val, name="predict"),
    path("incharge_profile", views.incharge_profile, name="incharge_profile")
]
