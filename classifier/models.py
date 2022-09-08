from fileinput import filename
from tkinter import CASCADE
import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class plantInformation(models.Model):
    scientificName = models.CharField(max_length=30, primary_key=True)
    localName = models.CharField(max_length=30)
    description = models.TextField()
    habitat = models.TextField()
    propagation = models.TextField()
    nativeRange = models.TextField()
    comments = models.TextField()
    control = models.TextField()
    date = models.DateField(auto_now_add=True)
    icon = models.TextField()

class classifier(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

class iasData(models.Model):
    requestnum = models.ForeignKey(
        classifier, 
        on_delete=models.CASCADE
        )
    scientificName = models.ForeignKey(
        plantInformation, 
        on_delete=models.CASCADE
        )
    latitude = models.FloatField(null=False)
    longtitude = models.FloatField(null=False)
    filename = models.CharField(max_length=200)
    filepath = models.TextField()

class tempFileHandler(models.Model):
    filename = models.CharField(max_length=200)
    latitude = models.FloatField(null=False)
    longtitude = models.FloatField(null=False)
    