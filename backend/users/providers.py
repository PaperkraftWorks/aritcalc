from users.models import User
from uuid import UUID
from typing import Optional


def get_user_by_id(user_id: UUID) -> Optional[User]:
    user = User.objects.filter(id=user_id)
    if user.exists():
        return user.first()
    return None