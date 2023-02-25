import enum
from dataclasses import dataclass


class Side(enum.Enum):
    BLACK = "black"
    WHITE = "white"


@dataclass
class Piece:
    x: int
    y: int
    side: Side



