from rest_framework import serializers
from classifier.models import classifier, plantInformation

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
            'comments',
            'control'
            ]

class classifier_Serializer(serializers.HyperlinkedModelSerializer):
    scientificName = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='scientificName'
     )
    username = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
     )
    class Meta:
        model = classifier
        fields = [
            'id',
            'date',
            'latitude',
            'longtitude',
            'filename',
            'filepath',
            'scientificName',
            'username',           
        ]
           