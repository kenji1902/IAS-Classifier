from django.urls import path
from . import views
urlpatterns = [
    path('filter/<fileName>', views.getBlobImage, name='getblobimage'),
    path('raw/<username>/<fileName>', views.getBlobImageRaw, name='getblobimageRaw'),
    path('icon/<fileName>', views.getIcon, name='geticon'),
    path('instruction/<fileName>', views.getInstructionImages, name='getinstructionimages'),
    path('getplant/<plantName>/<fileName>', views.getPlantImage, name='getplantimages'),

]