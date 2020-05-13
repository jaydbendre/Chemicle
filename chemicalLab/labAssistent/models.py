from django.db import models
from Lab.models import User
# Create your models here.


class FileLog(models.Model):
    file_name = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
