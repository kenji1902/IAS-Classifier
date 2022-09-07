from concurrent.futures import process
from distutils import extension
import pprint
import shutil
from unicodedata import name
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
import blobStorage

from classifier import morphologicalMask as morphMask
from classifier import geotagging as gt
import json
from django.http import HttpResponseBadRequest, JsonResponse
import cv2
import numpy as np
import base64
import os

from .models import classifier as clsfr
from django.contrib.auth.models import User
from .models import tempFileHandler, plantInformation
# Create your views here.
def classifier(request):
    if request.user.is_authenticated:
        return render(request,'classifier.html')
    else: 
        return redirect('/accounts/login/')
def results(request):
    return render(request,'results.html')

@ensure_csrf_cookie
def filter_files(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    username = request.user.username
    if(not os.path.isdir(f'static/blobStorage/images/temp/{username}/')):
        os.makedirs(f'static/blobStorage/images/temp/{username}/')

    if(not os.path.isdir(f'static/blobStorage/images/raw/{username}/')):
        os.makedirs(f'static/blobStorage/images/raw/{username}/')

    if is_ajax:
        if request.method == 'POST':
            files = request.FILES.getlist('files[]', None)
            coords = request.POST.getlist('coords[]')            
            uploadedFiles = []
            for f,c in zip(files,coords):
                uploadedFiles.append( handle_uploaded_file(request,f,c) )
            
            # files = os.listdir(f'static/blobStorage/images/temp/{username}/')
            return JsonResponse({'images': uploadedFiles})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def handle_uploaded_file(request,f,coords):
    username = request.user.username
    # Append _copy to file if it exists
    tempFileName = f'{username}-{f.name}'
    path = f'static/blobStorage/images/raw/{username}/'
    while(os.path.exists( os.path.join(path, tempFileName) )):
        file = tempFileName.split('.')
        extension = file[-1]
        file = ''.join(file[:-1])
        file = file+'_copy.'+extension
        tempFileName = file

    # Save per chunk, loop to save more memory
    filepath = os.path.join(path,tempFileName)
    with open(filepath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Save geolocation if it exists
    if(coords):
        coords = json.loads(coords)
        tempFileHandler.objects.create(filename=tempFileName, latitude=coords['lat'], longtitude=coords['lng'] )
    
    image = cv2.imread(filepath)
    path = f'static/blobStorage/images/temp/{username}/'
    filepath = os.path.join(path,tempFileName)
    image = cv2.resize(image, (256,256), interpolation = cv2.INTER_AREA)
    processImg = morphMask.morphologicalMasking(image)
    processImg = np.concatenate((np.array(image),np.array(processImg)),axis=2)
    processImg = morphMask.rgba2rgb(np.array(processImg))
    cv2.imwrite( filepath,processImg)
    return tempFileName


@ensure_csrf_cookie
def classify_files(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    username = request.user.username

    if is_ajax:
        if request.method == 'POST':
            images = request.POST.getlist('images[]')
            print(images)
            tempPath = f'static/blobStorage/images/temp/{username}/'
            rawPath = f'static/blobStorage/images/raw/{username}/'
    
            files = os.listdir(tempPath)            
            for file in files:
                if file not in images:
                    os.remove(tempPath+file)
                    os.remove(rawPath+file)
                    continue
                coords = gt.image_coordinates(rawPath+file,file)

                
            # Do the Classification/prediction here
            # 
            # 
            # add to database (id, username-fk, date, species name, local name, location, file name)
            #   
                
                clsfr.objects.create(
                    username = User.objects.get(username=username),
                    scientificName = plantInformation.objects.get(scientificName='test'),
                    latitude = coords['lat'],
                    longtitude = coords['lng'],
                    filename=file,
                    filepath=rawPath
                )

                print(file)
                print(json.dumps(coords, indent=4))
                
            # 
            # create a folder based on prediction name and move the images from temp folder   
            shutil.rmtree(tempPath)
            tempFileHandler.objects.all().delete()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')        

