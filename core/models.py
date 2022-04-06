from django.db import models
# from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

#Course 
class Course(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title