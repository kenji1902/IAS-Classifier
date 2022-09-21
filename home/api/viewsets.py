from rest_framework import viewsets
from home.models import instruction, instructionImages
from .serializers import instruction_Serializer, instructionImages_Serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class instruction_ViewSet(viewsets.ModelViewSet):
    queryset = instruction.objects.all()
    serializer_class = instruction_Serializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = [
        '$title',
        '$description'
    ]
    ordering_fields = ['instruction_order']


class instructionImages_ViewSet(viewsets.ModelViewSet):
    queryset = instructionImages.objects.all()
    serializer_class = instructionImages_Serializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]

    filterset_fields = [
        'instruction',
    ]
    ordering_fields = ['step']
