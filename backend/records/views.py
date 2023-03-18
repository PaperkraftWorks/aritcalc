from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from records.models import Record
from records.serializers import RecordSerializer
from rest_framework.generics import ListAPIView
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


class Records(ListAPIView):
    """
    List all code records, or create a new record.
    """
    serializer_class = RecordSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    queryset = Record.objects.all()
    permission_classes= [IsAuthenticated]
    
    def list(self, *args, **kwargs):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)