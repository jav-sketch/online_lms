from django.db import models
# from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

#Course 
class Course(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # created_at = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name