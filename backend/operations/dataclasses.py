from dataclasses import dataclass
from typing import Literal
from uuid import UUID

from operations.constants import TYPE_CHOICES


@dataclass
class OperationData():
    type:Literal[list(zip(*TYPE_CHOICES))[0]]
    id:UUID
    cost:int