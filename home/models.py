from email.mime import image
from django.db import models

# Create your models here.



class instruction(models.Model):
    instruction_order = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()

class instructionImages(models.Model):
    instruction = models.ForeignKey(instruction,on_delete=models.CASCADE)
    step = models.IntegerField()
    image = models.TextField(default=None)