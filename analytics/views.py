from django.shortcuts import render

# Create your views here.
def analytics(requests):
    return render(requests,'analytics.html')
