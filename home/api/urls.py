from django.urls import path, include
from rest_framework import routers
from .viewsets import instruction_ViewSet, instructionImages_ViewSet
router = routers.DefaultRouter()
router.register(r'instruction', instruction_ViewSet)
router.register(r'instructionimages', instructionImages_ViewSet)

urlpatterns = [
    path('', include(router.urls))
]