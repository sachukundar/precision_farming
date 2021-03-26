
from django.db import models 
  
# Create your models here. 
class Values(models.Model): 
    title = models.CharField(max_length = 30) 
    Temperature = models.IntegerField(default=0)
    Humidity = models.IntegerField(default=0) 
    Pressure =models.IntegerField(default=0)
    SMS=models.IntegerField(default=0)
    Date_Time=models.CharField(max_length = 30) 
    def __str__(self): 
        return self.title

