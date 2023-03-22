from uuid import UUID

from records import providers as records_providers
from records.dataclasses import RecordData

def get_last_record_by_user_id(user_id:UUID) -> RecordData:

    
    last_user_record_model = records_providers.get_last_record_by_user_id(user_id=user_id)
    if not last_user_record_model:
        return None
    last_user_record_data = RecordData(
        id=last_user_record_model.id ,
        operation_id=last_user_record_model.operation_id ,
        user_id=last_user_record_model.user_id ,
        user_balance=last_user_record_model.user_balance,
        amount=last_user_record_model.amount ,
        operation_response=last_user_record_model.operation_response ,
        date=last_user_record_model.date
    )
    return last_user_record_data

def create_record(
    operation_id: UUID,
    user_id: int,
    user_balance: int,
    amount: int,
    operation_response:str,) -> RecordData:
    record_object = records_providers.create_record(
        operation_id=operation_id,
        user_id=user_id,
        amount=amount,
        user_new_balance=user_balance,
        operation_response=operation_response
    )
    record_data = RecordData(
        id=record_object.id ,
        operation_id=record_object.operation_id ,
        user_id=record_object.user_id ,
        user_balance=record_object.user_balance,
        amount=record_object.amount ,
        operation_response=record_object.operation_response ,
        date=record_object.date
    )
    return record_data