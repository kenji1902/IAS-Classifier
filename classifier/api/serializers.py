from dataclasses import fields
from tkinter.tix import Tree
from rest_framework import serializers
from classifier.models import iasData, plantInformation, classifier, plantInformationImages
from django.contrib.auth.models import User
# Serializers define the API representation.


class plantInformationImages_Serializer(serializers.HyperlinkedModelSerializer):
    plantInformation = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field='scientificName'
    )
    class Meta:
        model = plantInformationImages
        fields = [
            'plantInformation',
            'order',
            'filename'
        ]

class plantInformation_Serializer(serializers.HyperlinkedModelSerializer):
    images = plantInformationImages_Serializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = plantInformation
        fields = [
            'scientificName', 
            'localName',
            'family', 
            'description', 
            'habitat',
            'propagation',
            'nativeRange',
            'invasiveType',
            'seedlingDispersionRadius',
            'comments',
            'control',
            'link',
            'date',
            'icon',
            'images',
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
            'points',
            'latitude',
            'longtitude',
            'reverseGeoLoc',
            'seedlingDispersionAffectedAreas',
            'filename',
            'filepath',
            'scientificName',
            'requestnum'
           
        ]
           