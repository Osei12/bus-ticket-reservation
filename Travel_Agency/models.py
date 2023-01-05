from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    destination = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.destination
    
class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    seats = models.IntegerField(null=False, blank=False)
    destination  = models.ForeignKey(Destination, on_delete=models.CASCADE)
    number_plate = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.bus_name

class BookBus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    bus = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=100)  
    email = models.CharField(max_length=100)  
    contact = models.CharField(max_length=100)
    destination = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
      