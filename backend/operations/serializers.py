from rest_framework import serializers
from operations.models import Operation

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Operation
        fields=[
            "id",
            "type",
            "cost"
        ]