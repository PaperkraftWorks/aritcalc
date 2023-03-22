from rest_framework.generics import ListAPIView
from rest_framework.settings import api_settings
from operations.models import Operation
from operations.serializers import OperationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
import re
from operations.services import get_operation_by_type
from records.business_rules import is_balance_for_operation_enough, get_last_user_balance_per_user_id
from records.services import create_record
from records.constants import INSUFICIENT_FUNDS_REASON, OK_REASON
import dataclasses

class Operations(ListAPIView):
    """
    List all code operations, or create a new record.
    """
    serializer_class = OperationSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    queryset = Operation.objects.all()
    permission_classes= [IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    
    
    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = OperationSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

class Builder(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes= [IsAuthenticated]
    
    def _translate_operations(self, operation:str):
        add=len(re.findall(r'[0-9]*(\+)[0-9]*', operation))
        sub=len(re.findall(r'[0-9]*(\-)[0-9]*', operation))
        div=len(re.findall(r'[0-9]*(\/)[0-9]*', operation))
        mul=len(re.findall(r'[0-9]*(\*)[0-9]*', operation))
        sqr=len(re.findall(r'[0-9]?(sqr\()[0-9]*', operation))
        rdm=len(re.findall(r'[0-9]?(rdm\()[0-9]*', operation))
        return {
            "ADD": add,
            "SUB": sub,
            "DIV": div,
            "MUL": mul,
            "SQR": sqr,
            "RDM": rdm,
        }
        
    def _get_operations_cost(self, operations):
        cost = 0
        for key in operations:
            if operations[key]:
                operation_data = get_operation_by_type(_type=key)
                operation_cost = operation_data.cost
                cost+= operations[key]*operation_cost
        return cost
    
    def get_general_cost(self, operations):
        cost = self._get_operations_cost(operations=operations)
        return cost
    
    def execute_operations(self, operations:dict, approved:bool, user_id:int):
        new_records = []
        for operation in operations:
            operation_data = get_operation_by_type(operation)
            for i in range(operations[operation]):
                last_balance = get_last_user_balance_per_user_id(user_id=user_id)
                new_balance = last_balance - operation_data.cost if approved else last_balance
                new_record = create_record(
                    operation_id=operation_data.id,
                    user_id=user_id,
                    user_balance=new_balance,
                    amount=operation_data.cost,
                    operation_response=OK_REASON if approved else INSUFICIENT_FUNDS_REASON
                )
                new_records.append(dataclasses.asdict(new_record))
        return new_records
        
                
    
    def post(self, request, *args, **kwargs):
        operation = request.data.get('operation')
        user = request.user
        operations = self._translate_operations(operation=operation)
        cost = self.get_general_cost(operations=operations)
        authorized = is_balance_for_operation_enough(cost=cost, user_id=user.id)
        new_records = self.execute_operations(operations=operations, approved=authorized, user_id=user.id)
        if not operation:
            return Response({})
        return Response({'authorized': authorized, 'records': new_records})
        