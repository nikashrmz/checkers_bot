import enum
from dataclasses import dataclass
from typing import Protocol


class Side(enum.Enum):
    BLACK = "black"
    WHITE = "white"


@dataclass
class Piece:
    x: int
    y: int
    side: Side



