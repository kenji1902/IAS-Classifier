from unicodedata import name
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

import json
from django.http import HttpResponseBadRequest, JsonResponse

# Create your views here.
def classifier(request):
    return render(request,'classifier.html',{'Name':'Kenji'})

@ensure_csrf_cookie
def upload_files(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            
            files = request.FILES.getlist('files[]', None)
            print('data here:', files)
            # for f in files:
            #     handle_uploaded_file(f)
            return JsonResponse({'status': 'uploaded successfuly'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)