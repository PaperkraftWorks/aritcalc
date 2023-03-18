from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass

class RecordData():
    id: UUID
    operation_id:UUID
    user_id:UUID
    amount:int
    user_balance:int
    operation_response:str
    date: datetime