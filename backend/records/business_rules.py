from typing import Optional
from uuid import UUID

from records import services as record_services


def get_last_user_balance_per_user_id(user_id: UUID) -> Optional[int]:
    last_user_record_data = record_services.get_last_record_by_user_id(user_id=user_id)
    if not last_user_record_data:
        return None
    return last_user_record_data.user_balance