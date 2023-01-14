from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=20, default = "20005074")
    password = models.CharField(max_length=20, default = "Password123")
    name = models.CharField(max_length=30, default = "Will")
    dob = models.CharField(max_length=10, default = "12/07/2002")
    phone = models.CharField(max_length=11, default = "07576928525")
    email = models.CharField(max_length=50, default = "william2.robertson@live.uwe.ac.uk")
    address = models.CharField(max_length=100, default = "BS1 1QY")


class Film(models.Model):
    title = models.CharField(max_length=100)
    ageRating = models.IntegerField()
    description = models.CharField(max_length=300)
    duration = models.CharField(max_length=12)

class Ticket(models.Model):
    title= models.ForeignKey(Film, null=True, default = None, related_name = 'titles', on_delete=models.SET_DEFAULT)
    ageRating = models.ForeignKey(Film, null=True, default = None, related_name = 'ages', on_delete=models.SET_DEFAULT)
    description = models.ForeignKey(Film, null=True, default = None, related_name = 'descriptions', on_delete=models.SET_DEFAULT)
    duration = models.ForeignKey(Film, null=True, default = None, related_name = 'durations', on_delete=models.SET_DEFAULT)
    totalCost = models.CharField(max_length=6, default = "£2.50")
    showingDate = models.CharField(max_length=10, default = "08/10/2023")
    showingTime= models.CharField(max_length=10, default = "14:00")
    seating = models.CharField(max_length=50, default = "[A,3]")