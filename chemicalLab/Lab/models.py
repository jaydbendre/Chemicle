from django.db import models

class Role(models.Model):
    post = models.CharField(max_length= 20)

class Department(models.Model):
    name = models.CharField(max_length= 20)

class Lab(models.Model):
    name = models.CharField(max_length= 20)
    dept_id = models.ForeignKey(Department, on_delete = models.CASCADE)

class User(models.Model):
    fname = models.CharField(max_length= 30)
    lname = models.CharField(max_length= 30)
    email = models.EmailField()
    password = models.CharField(max_length= 500)
    address = models.CharField(max_length= 100)
    role_id = models.ForeignKey(Role, on_delete = models.CASCADE, default = 2)
    lab_id = models.ForeignKey(Lab , on_delete = models.CASCADE , default = None)

class Request(models.Model):
    description = models.TextField(max_length = 1000)
    request_from = models.ForeignKey(User, on_delete = models.CASCADE)
    #Add foreign key to user table
    request_to = models.IntegerField()
    humidity = models.FloatField()
    temperature = models.FloatField()

class Notification(models.Model):
    Notification_to = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField(max_length = 1000)
    timestamp = models.DateField(auto_now_add = True)
    category = models.CharField(max_length = 100)

class Sensor_log(models.Model):
    lab_id = models.ForeignKey(Lab, on_delete = models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField() 
    air_quality = models.FloatField()
    timestamp = models.DateField(auto_now_add = True)
