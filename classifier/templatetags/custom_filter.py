from django import template
from accounts.models import voteResults

from classifier.models import iasData, plantInformationImages
register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)

@register.simple_tag(name='loadPlantImage')
def loadPlantImage(plant):
    return plantInformationImages.objects.filter(plantInformation = plant)

@register.simple_tag(name='checkuservotes')
def checkuservotes(id, user ,vote):
    
    try:
        print(id,user,'vote: ',vote)
        query = voteResults.objects.get(iasdata_id=id,user_id=user)
        if query.type == vote:
            return True
    except voteResults.DoesNotExist:
        return False
    return False
