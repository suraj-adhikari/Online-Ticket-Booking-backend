from enum import unique
from django.db import models

class movieticket(models.Model):
    movie_name = models.CharField(max_length=200)
    releasing_date= models.DateField(auto_now=True)
    description = models.CharField(max_length=1000)
    movie_timings = models.DateTimeField(auto_now=True)
    make_payment = models.BooleanField()
    # select_seat = models.IntegerField( unique=True)
