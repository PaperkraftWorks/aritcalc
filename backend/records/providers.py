from records.models import Record
from uuid import UUID
from typing import Optional


def create_record(operation_id:UUID, user_id:str, amount:int, user_new_balance:int, operation_response: str) -> Optional[Record]:
    
    new_record = Record.objects.create(
        operation_id=operation_id,
        user_id=user_id,
        amount=amount,
        user_balance=user_new_balance,
        operation_response=operation_response
    )
    return new_record

def get_last_record_by_user_id(user_id:UUID) -> Optional[Record]:
    
    record = Record.objects.filter(user_id=user_id).order_by("-date")
    if record.exists():
        return record.first()
    return None