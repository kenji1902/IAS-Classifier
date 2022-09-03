from concurrent.futures import process
from distutils import extension
from unicodedata import name
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
import blobStorage

from classifier import morphologicalMask as morphMask
import json
from django.http import HttpResponseBadRequest, JsonResponse
import cv2
import numpy as np
import base64
import os
# Create your views here.
def classifier(request):
    return render(request,'classifier.html',{'Name':'Kenji'})

@ensure_csrf_cookie
def filter_files(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            files = request.FILES.getlist('files[]', None)
            for f in files:
                image = cv2.imdecode(np.fromstring(f.read(), np.uint8), cv2.IMREAD_UNCHANGED)
                image = cv2.resize(image, (256,256), interpolation = cv2.INTER_AREA)
                processImg = morphMask.morphologicalMasking(image)
                processImg = np.concatenate((np.array(image),np.array(processImg)),axis=2)
                processImg = morphMask.rgba2rgb(np.array(processImg))
                handle_uploaded_file(processImg,f.name)
            files = os.listdir('static/blobStorage/images/')
            return JsonResponse({'images': files})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

@ensure_csrf_cookie
def classify_files(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            images = request.POST.getlist('images[]')
            files = os.listdir('static/blobStorage/images/')
            for f in files:
                if f not in images:
                    os.remove("static/blobStorage/images/"+f)

            # Classify here   
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')        

def handle_uploaded_file(processImg,name):
    path = os.path.join('static/blobStorage/images',name)
    while(os.path.exists(path)):
        filePath = path.split('.')
        extension = filePath[-1]
        filePath = filePath[-2]
        filePath = filePath+'_copy.'+extension
        path = filePath

    cv2.imwrite(path,processImg)
        