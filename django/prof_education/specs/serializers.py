from rest_framework import serializers

from .models import Specialization, EducationDirection


class EducationDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDirection
        fields = serializers.ALL_FIELDS


class SpecializationSerializer(serializers.ModelSerializer):
    directions = EducationDirectionSerializer(many=True)

    class Meta:
        model = Specialization
        fields = serializers.ALL_FIELDS
