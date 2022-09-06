from django.urls import path
from . import views
urlpatterns = [
    path('blobstorage/<fileName>', views.getBlobImage, name='getblobimage'),
]