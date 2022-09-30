from msilib.schema import Icon
from django.shortcuts import render
from classifier.models import *
from django.conf import settings
# Create your views here.
def information(request):
    plantsFields = plantInformation.objects.values_list("scientificName",'localName','icon')
    local = []
    scientific = []
    Icons = []    
    for a,b,c in plantsFields:
        scientific.append(a)
        local.append(b)
        Icons.append(c)
    HOST = settings.GMAP_LOCAL_API_KEY
    if request.META['HTTP_HOST'] == 'condescending-fog-39986.pktriot.net' and settings.ENABLED_API_KEY:
        HOST = settings.GMAP_API_KEY
    count = classifier.objects.all().count()
    return render(request,'information.html',{
        'scientific':scientific,
        'local':local,
        'totalRecords' : count,
        'plants' : zip(Icons,scientific,local),
        'GMAP_KEY':HOST
    })