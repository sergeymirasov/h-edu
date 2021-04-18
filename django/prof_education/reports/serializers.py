from rest_framework import serializers

from .models import SavedReport


class DataSourceSerializer(serializers.Serializer):
    name = serializers.CharField()
    label = serializers.CharField()


class SlitSerializer(serializers.Serializer):
    name = serializers.CharField()
    label = serializers.CharField()


class ColumnSetItemSerializer(serializers.Serializer):
    column_key = serializers.CharField()
    formats = serializers.ListField(child=serializers.CharField())


class ColumnSetSerializer(serializers.Serializer):
    label = serializers.CharField()
    items = ColumnSetItemSerializer(many=True)


class SavedReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedReport
        fields = serializers.ALL_FIELDS
