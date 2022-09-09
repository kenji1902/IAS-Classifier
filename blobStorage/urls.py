from django.urls import path
from . import views
urlpatterns = [
    path('filter/<fileName>', views.getBlobImage, name='getblobimage'),
    path('raw/<username>/<fileName>', views.getBlobImageRaw, name='getblobimageRaw'),
]