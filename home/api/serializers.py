from dataclasses import fields
from rest_framework import serializers
from home.models import instruction, instructionImages

class instruction_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = instruction
        fields = [
            'id',
            'order',
            'title',
            'description'
        ]

class instructionImages_Serializer(serializers.HyperlinkedModelSerializer):
    instruction = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field='id'
    )
    class Meta:
        model = instructionImages
        fields = [
            'instruction',
            'step',
            'image'
        ]