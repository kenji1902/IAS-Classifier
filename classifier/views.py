from concurrent.futures import process
from distutils import extension
import pprint
import shutil
from textwrap import indent
from unicodedata import name
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core import serializers
from django.http import HttpResponseBadRequest, JsonResponse

from classifier import morphologicalMask as morphMask
from classifier import geotagging as gt
from classifier.CNNkNN import classifier as cnnknn, constants

import json
import cv2
import numpy as np
import base64
import os
from datetime import date

from .models import classifier as clsfr
from .models import iasData
from django.contrib.auth.models import User
from .models import tempFileHandler, plantInformation
# Create your views here.
def classifier(request):
    if request.user.is_authenticated:
        return render(request,'classifier.html')
    else: 
        return redirect('/accounts/login/')
def results(request,pk):
    username = request.user.username
    try:
        query = iasData.objects.filter(requestnum = pk)
        # serialized_queryset = serializers.serialize('json', query,indent=4)
        
        if username == str(query[0].requestnum.username) or username=='admin':
            return render(request,'results.html',{'data':query})
        return HttpResponseBadRequest('Invalid request')    
    except IndexError:
        return HttpResponseBadRequest('Invalid request')        

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
    tempFileName = f'{date.today()}-{f.name}'
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
    image,_ = morphMask.auto_crop(image)
    image = cv2.resize(image, (256,256), interpolation = cv2.INTER_AREA)
    processImg,Mask = morphMask.morphologicalMasking(image)
    
    cv2.imwrite( filepath,processImg)
    return tempFileName


@ensure_csrf_cookie
def classify_files(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    username = request.user.username
    classifier_models = []
    
    if is_ajax:
        if request.method == 'POST':
            knn, model_feat = cnnknn.loadData()
            requestnum = clsfr.objects.create(
                username = User.objects.get(username=username),
            )
            images = request.POST.getlist('images[]')
            print(images)
            tempPath = f'static/blobStorage/images/temp/{username}/'
            rawPath = f'static/blobStorage/images/raw/{username}/'
    
            files = os.listdir(tempPath)
            processImgNP = []    
            for file in files:
                if file not in images:
                    os.remove(tempPath+file)
                    os.remove(rawPath+file)
                    continue
                image = cv2.imread(tempPath+file)
                processImgNP.append(image)
            processImgNP = np.array(processImgNP)    
            predictions = cnnknn.predict(processImgNP,model_feat,knn)
            print('predictions: ',predictions)
            files = os.listdir(tempPath)
            for file, prediction in zip(files,predictions):
                coords = gt.image_coordinates(rawPath+file,file)

                
                # Do the Classification/prediction here
                
             
                # add to database (id, username-fk, date, species name, 
                # local name, location, file name)
               
                # print(prediction)
                iasData.objects.create(
                    requestnum = clsfr.objects.get(id=requestnum.id),  
                    scientificName = plantInformation.objects.get(scientificName=prediction),
                    latitude = coords['lat'],
                    longtitude = coords['lng'],
                    filename=file,
                    filepath=f'blobStorage/images/raw/{username}/'
                )
                print(file)
                print(json.dumps(coords, indent=4))
            # print(predictions)
     
            # 
            # create a folder based on prediction name and move the images from temp folder   
            shutil.rmtree(tempPath)
            tempFileHandler.objects.all().delete()
            return JsonResponse({'id':requestnum.id})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')        

