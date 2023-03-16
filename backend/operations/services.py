from typing import Literal, Optional, List

from operations import dataclasses as operations_dataclasses
from operations import providers as operations_providers
from operations.constants import TYPE_CHOICES


def get_operation_by_type(_type:Literal[list(zip(*TYPE_CHOICES))[0]]) -> Optional[operations_dataclasses.OperationData]:
    operation_model = operations_providers.get_operation_by_type(_type=_type)
    if not operation_model:
        return None
    operation_data = operations_dataclasses.OperationData(
        type=operation_model.type,
        id=operation_model.id,
        cost=operation_model.cost,
    )
    return operation_data

def get_operation_cost_list_by_type(operation_types:List[str]) -> Optional[List[int]]:
    operation_qs = operations_providers.filter_operation_by_type(operation_types=operation_types)
    if operation_qs is None:
        return None
    return list(operation_qs.values_list("cost", flat=True))
