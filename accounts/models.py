from email.policy import default
from random import choices
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from classifier.models import iasData

# Create your models here.

class Authentication(models.Model):
    class position(models.TextChoices):
        none = None,_('-----')
        bachelor = 'bachelor',_('bachelor')
        masteral = 'masteral',_('masteral')
        doctorate = 'doctorate',_('doctorate')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    educationalAttainment = models.CharField(max_length=10, choices=position.choices, null=True, default=None)
    proof = models.TextField(null=True, default=None, blank=True)
    is_authenticated = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)

class voteResults(models.Model):
    class votetype(models.TextChoices):
        none = None,_('-----')
        up = 'up',_('up')
        down = 'down',_('down')

    iasdata_id = models.ForeignKey(iasData,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    type= models.CharField(max_length=5,choices=votetype.choices, null=True, default=None)




from django.db.models.signals import pre_delete,post_delete
from classifier.models import iasData
from django.dispatch import receiver
from classifier import constants as c
@receiver(pre_delete, sender=voteResults)
def pre_delete_votes(sender, instance,*args, **kwargs):
    print('deleting id:',instance.id," |ias id: ", instance.iasdata_id.id, " | User: ",instance.user_id)
    iasdata = iasData.objects.get(id = instance.iasdata_id.id)
    auth = Authentication.objects.get(user = instance.user_id)
    authpoints = c.pointSystem[auth.educationalAttainment]
    if instance.type == 'up':
        iasdata.points -= authpoints
    elif instance.type == 'down':
        iasdata.points += authpoints

    iasdata.save()
