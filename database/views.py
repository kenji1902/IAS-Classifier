import imp
from xml.etree.ElementInclude import include
from django.shortcuts import render
from accounts.models import voteResults
from classifier.models import *
from django.contrib.auth.models import User
from django.http import Http404
import json
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from classifier import constants as c
from accounts.models import Authentication, voteResults

# Create your views here.
def viewDatabase(request):
    plantsFields = plantInformation.objects.values_list("scientificName",'localName')
    local = []
    scientific = []
    uservotes = {}
    for i in voteResults.objects.filter(user_id=request.user.id):
        uservotes[i.iasdata_id.id] = i.type,
         
    for a,b in plantsFields:
        scientific.append(a)
        local.append(b)

    count = classifier.objects.all().count()
    return render(request,'databaseResults.html',{
        'scientific':scientific,
        'local':local,
        'totalRecords' : count,
        'uservotes':json.dumps( uservotes),
    })

def viewPlant(request,pk):
    try:
        query = iasData.objects.get(id = pk)
        # serialized_queryset = serializers.serialize('json', query,indent=4)
        plants = plantInformation.objects.values_list('scientificName')
        return render(request,'plantPK.html',{'data':query,'plants':plants})
    except iasData.DoesNotExist:
        raise Http404  
def getvote(request, iasdata_id):
    if request.method == 'GET':
        try:
            return JsonResponse({'type':voteResults.objects.get(
                user_id=request.user.id, 
                iasdata_id= iasdata_id).type,
                'iasdata_id':iasdata_id
                })
        except voteResults.DoesNotExist:
            return JsonResponse({'type':'none','iasdata_id':iasdata_id})
@ensure_csrf_cookie
def votecount(request):

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            try:
                currentUser = request.user
                educationalAttainment = Authentication.objects.get(user_id=currentUser.id).educationalAttainment
                if c.pointSystem.get(educationalAttainment):
                    voteType = request.POST.get('type')
                    id = request.POST.get('id')
                    query = None
                    switchvoteFlag = False
                    try:
                        query = voteResults.objects.get(user_id = currentUser, iasdata_id = id)
                        if query.type == voteType:
                            query.type = 'none'
                        else:
                            if query.type != 'none':
                                switchvoteFlag = True
                            query.type = voteType
                           
                        query.save()
                    except voteResults.DoesNotExist:
                        query = voteResults.objects.create(
                            user_id = User.objects.get(username=currentUser),
                            iasdata_id = iasData.objects.get(id=id),
                            type = voteType
                        )
                    
                    iasobj = iasData.objects.get(id=id)
                    # point = (voteResults.objects.filter(iasdata_id = id, type='up').count() - voteResults.objects.filter(iasdata_id = id, type='down').count() ) * c.pointSystem[educationalAttainment] 
                    # iasobj.points = point                    
                    # iasobj.save()
                    if switchvoteFlag:
                        if query.type == 'up':
                            iasobj.points += c.pointSystem[educationalAttainment] * 2
                        elif query.type == 'down' :
                            iasobj.points -= c.pointSystem[educationalAttainment] * 2

                    elif query.type == 'up':
                        iasobj.points += c.pointSystem[educationalAttainment]
                    elif query.type == 'down' :
                        iasobj.points -= c.pointSystem[educationalAttainment]
                    else:
                        if voteType == 'up':
                            iasobj.points -= c.pointSystem[educationalAttainment]
                        elif voteType == 'down' :
                            iasobj.points += c.pointSystem[educationalAttainment]
                    iasobj.save()
                    
                    
                    
                    
                    return JsonResponse({'status':iasobj.points})
            except Authentication.DoesNotExist:
                return JsonResponse({'status': 'Invalid request'}, status=300)
    return JsonResponse({'status': 'Invalid request'}, status=300)  

def refreshvotepoints(request,iasdata_id):
    if request.method == 'GET':
        try:
            auth = Authentication.objects.all()
            for i in auth:
                educationalAttainment = i.educationalAttainment
                if c.pointSystem.get(educationalAttainment):   
                    iasobj = iasData.objects.get(id=iasdata_id)
                    point = (voteResults.objects.filter(iasdata_id = iasdata_id, type='up').count() - voteResults.objects.filter(iasdata_id = iasdata_id, type='down').count() ) * c.pointSystem[educationalAttainment] 
                    iasobj.points = point                    
                    iasobj.save()
                
                return JsonResponse({'status':iasobj.points})
        except Authentication.DoesNotExist:
            return JsonResponse({'status': 'Invalid request'}, status=300)
    return JsonResponse({'status':'Invalid request'})

def get_model_fields(model):
    return [f.name for f in model._meta.get_fields()]

def handler404(request, exception):
    return render(request,'404.html')