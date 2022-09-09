from rest_framework import viewsets
from classifier.models import classifier, plantInformation, iasData
from .serializers import plantInformation_Serializer, classifier_Serializer, iasData_Serializer
from django_filters.rest_framework import DjangoFilterBackend
# ViewSets define the view behavior.
class plantInformation_ViewSet(viewsets.ModelViewSet):
    queryset = plantInformation.objects.all()
    serializer_class = plantInformation_Serializer

class classifier_ViewSet(viewsets.ModelViewSet):
    queryset = classifier.objects.all()
    serializer_class = classifier_Serializer

class iasData_ViewSet(viewsets.ModelViewSet):
    queryset = iasData.objects.all()
    serializer_class = iasData_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'requestnum',
        'scientificName__scientificName',
        'scientificName__localName',  
        'requestnum__username__username'
    ]
