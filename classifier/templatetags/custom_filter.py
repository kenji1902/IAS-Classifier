from django import template

from classifier.models import plantInformationImages
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