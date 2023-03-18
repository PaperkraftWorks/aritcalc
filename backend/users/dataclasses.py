from dataclasses import dataclass
from typing import Literal
from uuid import UUID


@dataclass
class UserData():
    id: UUID
    username:str
    status:Literal['O', "I"]