from typing import Optional
from uuid import UUID

from users import providers as users_providers
from users.dataclasses import UserData


def get_user_by_id(user_id:UUID) -> Optional[UserData]:
    user_obj = users_providers.get_user_by_id(user_id=user_id)
    if not user_obj:
        return None
    user_data = UserData(
        id=user_obj.id,
        username=user_obj.username,
        status=user_obj.status,
    )
    return user_data