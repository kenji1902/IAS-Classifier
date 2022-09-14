from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import cv2
import base64

# Create your views here.

def getBlobImage(request,fileName):
    # is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    # if is_ajax:
    #     if request.method == 'GET':
    image_data = open(f'static/blobStorage/images/temp/{request.user.username}/{fileName}', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")    

def getBlobImageRaw(request,username,fileName):
    image_data = open(f'static/blobStorage/images/raw/{username}/{fileName}', "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")          


def getIcon(request,fileName):
    image_data = open(f'static/blobStorage/images/icons/{fileName}', "rb").read()
    return HttpResponse(image_data, content_type="image/png")        