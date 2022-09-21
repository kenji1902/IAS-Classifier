from dataclasses import fields
from rest_framework import serializers
from home.models import instruction, instructionImages

class instruction_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = instruction
        fields = [
            'instruction_order',
            'title',
            'description'
        ]

class instructionImages_Serializer(serializers.HyperlinkedModelSerializer):
    instruction = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field='instruction_order'
    )
    class Meta:
        model = instructionImages
        fields = [
            'instruction',
            'step',
            'image'
        ]