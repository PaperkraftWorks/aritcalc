from typing import Optional, List
from uuid import UUID

from records import services as record_services
from records.constants import (INSUFICIENT_FUNDS_REASON,USER_DOES_NOT_EXIST_REASON, OK_REASON)
from operations import services as operation_services

def get_last_user_balance_per_user_id(user_id: UUID) -> Optional[int]:
    last_user_record_data = record_services.get_last_record_by_user_id(user_id=user_id)
    if not last_user_record_data:
        return None
    return last_user_record_data.user_balance

def is_balance_for_operation_enough(cost:int, user_id:UUID) -> Optional[bool]:
    """
    This Business rule checks if user has balance for a calculation
    cost:: big5int::
    user_id :: uuid:: user uuid identification 
    """
    last_balance = get_last_user_balance_per_user_id(user_id=user_id)
    if not last_balance:
        return None
    return last_balance>=cost

def generate_response(authorized:Optional[bool])-> dict:
    if authorized is None:
        reason = USER_DOES_NOT_EXIST_REASON
    elif authorized is False:
        reason = INSUFICIENT_FUNDS_REASON
    else:
        reason = OK_REASON
    return {
        "authorized":authorized,
        "reason": reason
    }

def total_cost(operation_type_list:List[str])-> int:
    operation_cost_hash = {
        operation_type:operation_services.get_operation_by_type(operation_type).cost for operation_type in set(operation_type_list)
    }
    return sum([operation_cost_hash[operation] for operation in operation_type_list])