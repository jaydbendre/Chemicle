from django.db import models
import datetime


class Role(models.Model):
    post = models.CharField(max_length=20)


class Department(models.Model):
    name = models.CharField(max_length=20)


class Lab(models.Model):
    name = models.CharField(max_length=20)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)


class User(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=100)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, default=2)
    lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE, default=None)


class Request(models.Model):
    description = models.TextField(max_length=1000)
    request_from = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add foreign key to user table
    request_to = models.IntegerField()
    humidity = models.FloatField()
    temperature = models.FloatField()


class Notification(models.Model):
    Notification_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Sender")
    Notification_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Reciever")
    description = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    delete_field = models.BooleanField(default=False)

    class Meta:
        ordering = ["-timestamp"]

    @classmethod
    def create_notification(cls, to, by, description, category):
        notif = Notification(Notification_to=to, Notification_by=by,
                             description=description, timestamp=datetime.datetime.now(),
                             category=category, delete_field=False)
        notif.save()


class Sensor_log(models.Model):
    lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    air_quality = models.FloatField()
    timestamp = models.DateField(auto_now_add=True)


class Schedule(models.Model):
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(auto_now_add=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default=None)
    event_type = models.IntegerField(default=1)
    title = models.TextField(default=None)
