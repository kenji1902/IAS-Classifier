from django.urls import path, include
from rest_framework import routers
from .viewsets import classifier_ViewSet, plantInformation_ViewSet, iasData_ViewSet, plantInformationImages_ViewSet

router = routers.DefaultRouter()
router.register(r'plantinformation', plantInformation_ViewSet)
router.register(r'plantinformationImages', plantInformationImages_ViewSet)
router.register(r'classifier', classifier_ViewSet)
router.register(r'iasdata', iasData_ViewSet)

urlpatterns = [
    path('', include(router.urls))
]
