from rest_framework import viewsets
from classifier.models import classifier, plantInformation, iasData
from .serializers import plantInformation_Serializer, classifier_Serializer, iasData_Serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class plantInformation_ViewSet(viewsets.ModelViewSet):
    queryset = plantInformation.objects.all()
    serializer_class = plantInformation_Serializer

class classifier_ViewSet(viewsets.ModelViewSet):
    queryset = classifier.objects.all()
    serializer_class = classifier_Serializer

class iasData_ViewSet(viewsets.ModelViewSet):
    queryset = iasData.objects.all()
    serializer_class = iasData_Serializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = [
        'id',
        'requestnum',
        'requestnum__date',
        'scientificName__scientificName',
        'scientificName__localName',
        'scientificName__invasiveType',  
        'requestnum__username__username'
    ]
    search_fields = [
        'scientificName__scientificName',
        'scientificName__localName',  
    ]
