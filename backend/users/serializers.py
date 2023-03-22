from rest_framework import serializers
from users.models import MainUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainUser
        fields=[
            "id",
            "username",
            "status"
        ]
    