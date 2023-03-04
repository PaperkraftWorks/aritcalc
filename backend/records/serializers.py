from rest_framework import serializers
from records.models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Record
        fields = [
            "id",
            "amount",
            "user_balance",
            "operation_response",
            "date",
            "operation_id",
            "user_id"
        ]
        