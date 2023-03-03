from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from operations.models import Operation
from operations.serializers import OperationSerializer


def operation_list(request):
    """
    List all code operations, or create a new record.
    """
    if request.method == 'GET':
        operations = Operation.objects.all()
        serializer = OperationSerializer(operations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OperationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)