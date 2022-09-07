from rest_framework import viewsets
from classifier.models import classifier, plantInformation
from .serializers import plantInformation_Serializer, classifier_Serializer

# ViewSets define the view behavior.
class plantInformation_ViewSet(viewsets.ModelViewSet):
    queryset = plantInformation.objects.all()
    serializer_class = plantInformation_Serializer

class classifier_ViewSet(viewsets.ModelViewSet):
    queryset = classifier.objects.all()
    serializer_class = classifier_Serializer