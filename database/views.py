import imp
from xml.etree.ElementInclude import include
from django.shortcuts import render
from classifier.models import *
from django.contrib.auth.models import User
from django.http import Http404

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

def viewPlant(request,pk):
    try:
        query = iasData.objects.get(id = pk)
        # serialized_queryset = serializers.serialize('json', query,indent=4)
        plants = plantInformation.objects.values_list('scientificName')
        return render(request,'plantPK.html',{'data':query,'plants':plants})
    except iasData.DoesNotExist:
        print('hello')
        raise Http404  


def get_model_fields(model):
    return [f.name for f in model._meta.get_fields()]

def handler404(request, exception):
    return render(request,'404.html')