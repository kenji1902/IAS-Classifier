from email.policy import default
from fileinput import filename
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class plantInformation(models.Model):
    class invasiveType(models.TextChoices):
        invasive = 'invasive',_('invasive')
        exotic = 'exotic',_('exotic')

    scientificName = models.CharField(max_length=30, primary_key=True)
    localName = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    description = models.TextField()
    habitat = models.TextField()
    propagation = models.TextField()
    nativeRange = models.TextField()
    invasiveType = models.CharField(max_length=10,choices=invasiveType.choices)
    seedlingDispersionRadius = models.IntegerField(default=1000)
    comments = models.TextField()
    control = models.TextField()
    link = models.TextField(null=True)
    date = models.DateField(auto_now=True)
    icon = models.TextField()

class plantInformationImages(models.Model):
    plantInformation = models.ForeignKey(
        plantInformation,
        on_delete = models.CASCADE,
        related_name='images'
    )
    order = models.IntegerField()
    filename = models.CharField(max_length=200)
    class Meta:
        ordering = ['order']
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
    reverseGeoLoc = models.TextField(null=False)
    seedlingDispersionAffectedAreas = models.TextField(null=True)
    filename = models.CharField(max_length=200)
    filepath = models.TextField()
 

class tempFileHandler(models.Model):
    filename = models.CharField(max_length=200)
    latitude = models.FloatField(null=False)
    longtitude = models.FloatField(null=False)
    