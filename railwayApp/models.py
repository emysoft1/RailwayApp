from django.db import models
from django.contrib.auth.models import User
import uuid

class Station(models.Model):
    name_of_station = models.CharField(max_length=255)
    location = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_station

class Train(models.Model):
    CHOICES = (
        ('Economy', 'Economy'),
        ('Vip', 'Vip'),
        ('Others', 'Others'),
    )
    name_of_train = models.CharField(max_length=255)
    train_number = models.CharField(max_length=255)
    station = models.ForeignKey('Station', on_delete=models.CASCADE,)
    route = models.ForeignKey('Route', on_delete=models.CASCADE,)
    available_seat=models.IntegerField()
    seat_type = models.CharField(choices=CHOICES, max_length=255)
    departure_time = models.TimeField(auto_now=False, auto_now_add=False)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return "%s %s"%(self.name_of_train, self.route)

class Route(models.Model):
    source = models.ForeignKey('Station', on_delete=models.CASCADE, related_name='From')
    destination = models.ForeignKey('Station', on_delete=models.CASCADE, related_name='to')
    price = models.DecimalField(decimal_places=2, default=0.0, max_digits=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s %s"%(self.source, self.destination)


class Reservation(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )

    STATUS = (
        ('Adult', 'Adult'),
        ('Child', 'Child'),
        ('Others', 'Others'),
    )
    full_name = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS, max_length=255)
    no_of_person = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=255)
    ticket_number = models.CharField(max_length=36, default=uuid.uuid4)
    Journey = models.ForeignKey(Route, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Titles(models.Model):
    text_title = models.CharField(max_length=255, default='text')
    sub_title = models.CharField(max_length=255,default='text')

   
    



