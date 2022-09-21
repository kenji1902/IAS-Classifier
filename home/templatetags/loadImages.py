from django import template
from home.models import instructionImages

register = template.Library()
@register.simple_tag(name='loadimages')
def loadimages(pk):
    return instructionImages.objects.filter(instruction=pk).order_by('step').values()
    
