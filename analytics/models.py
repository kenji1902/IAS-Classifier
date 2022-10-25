from email.policy import default
from django.db import models

# Create your models here.
class plantreports(models.Model):
    date = models.DateField(auto_now=True,primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    chartdata = models.TextField()
    active = models.BooleanField(default=False)