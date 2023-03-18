from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializers import UserSerializer



class Users(ListAPIView):
    """
    List all code operations, or create a new record.
    """
    serializer_class = UserSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    queryset = User.objects.all()
    permission_classes= [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
