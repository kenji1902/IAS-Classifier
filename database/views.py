import imp
from xml.etree.ElementInclude import include
from django.shortcuts import render
from classifier.models import *
from django.contrib.auth.models import User
# Create your views here.
def viewDatabase(request):
    plantsFields = plantInformation.objects.values_list("scientificName",'localName')
    local = []
    scientific = []    
    for a,b in plantsFields:
        scientific.append(a)
        local.append(b)

    count = classifier.objects.all().count()
    print(scientific,local)
    return render(request,'databaseResults.html',{
        'scientific':scientific,
        'local':local,
        'totalRecords' : count
    })


def get_model_fields(model):
    return [f.name for f in model._meta.get_fields()]