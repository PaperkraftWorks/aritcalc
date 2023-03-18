from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from rest_framework.settings import api_settings
from operations.models import Operation
from operations.serializers import OperationSerializer
from rest_framework.permissions import IsAuthenticated


class Operations(ListAPIView):
    """
    List all code operations, or create a new record.
    """
    serializer_class = OperationSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    queryset = Operation.objects.all()
    permission_classes= [IsAuthenticated]
    
    
    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = OperationSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
