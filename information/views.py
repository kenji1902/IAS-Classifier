from msilib.schema import Icon
from django.shortcuts import render
from classifier.models import *
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

    count = classifier.objects.all().count()
    return render(request,'information.html',{
        'scientific':scientific,
        'local':local,
        'totalRecords' : count,
        'plants' : zip(Icons,scientific,local)
    })