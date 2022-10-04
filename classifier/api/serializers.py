from tkinter.tix import Tree
from rest_framework import serializers
from classifier.models import iasData, plantInformation, classifier
from django.contrib.auth.models import User
# Serializers define the API representation.
class plantInformation_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = plantInformation
        fields = [
            'scientificName', 
            'localName', 
            'description', 
            'habitat',
            'propagation',
            'nativeRange',
            'invasiveType',
            'comments',
            'control',
            'date',
            'icon',
            ]



class classifier_Serializer(serializers.HyperlinkedModelSerializer): 
    username = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field='username'
    )
    class Meta:
        model = classifier
        fields = [
            'id',
            'username',
            'date'
        ]

class iasData_Serializer(serializers.HyperlinkedModelSerializer):
    scientificName = plantInformation_Serializer(
        many=False,
        read_only=True
     )
    requestnum = classifier_Serializer(
        many=False,
        read_only=True
     )
    class Meta:
        model = iasData
        fields = [
            'id',
            'latitude',
            'longtitude',
            'reverseGeoLoc',
            'seedlingDispersionAffectedAreas',
            'filename',
            'filepath',
            'scientificName',
            'requestnum'
           
        ]
           