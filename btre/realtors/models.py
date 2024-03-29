from django.db import models
from datetime import datetime

class Realtor(models.Model):
    
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(datetime.now, blank=True)
    
    def __str__(self):
        return self.name
    
    
