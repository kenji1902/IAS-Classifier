from django.shortcuts import render

from analytics.models import plantreports

# Create your views here.
def analytics(requests):
    datareport = None
    try:
        datareport = plantreports.objects.filter(active=True).last()
        print(datareport)
    except plantreports.DoesNotExist:
        pass
    return render(requests,'analytics.html', {'datareport':datareport})
