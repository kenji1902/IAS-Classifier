from django.shortcuts import render
import json, os
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse

from accounts.models import Authentication
# Create your views here.

def authenticate(request):
    return render(request,'account/authenticate.html')

def validateCredentials(request):
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            username = request.user
            eduAttainment = request.POST.get('eduAttainment')
            file = request.FILES['file']
            

            handle_uploaded_file(username,eduAttainment,file)
           
            return JsonResponse({'status':'success'})
    return JsonResponse({'status': 'Invalid request'}, status=400)
    
def handle_uploaded_file(username,edu,f):
    path = f'static/blobstorage/userapplication/{username}/'
    filename = f'{edu}-{f.name}'
    filepath = f'{path}{filename}'
    if(not os.path.isdir(path)):
        os.makedirs(path)

    with open(filepath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    userData = Authentication.objects.get(user_id=username.id)
    userData.educationalAttainment = edu
    userData.proof = filename
    userData.is_pending = True
    userData.save()