from typing import Literal, Optional

from operations import models as operations_models
from operations.constants import TYPE_CHOICES


def get_operation_by_type(_type:Literal[list(zip(*TYPE_CHOICES))[0]])-> Optional[operations_models.Operation]:
    operator_model = operations_models.Operation.objects.filter(type=_type)
    if not operator_model.exists():
        return None
    return operator_model.first()

