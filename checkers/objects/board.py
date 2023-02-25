from typing import List

from checkers.objects.piece import Piece, Side


class Board:
    slots: List[List[Piece]] = [[None for i in range(8)] for j in range(8)]

    def __init__(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    if i not in [3, 4]:
                        if i < 4:
                            self.slots[i][j] = Piece(i, j, Side.BLACK)
                        else:
                            self.slots[i][j] = Piece(i, j, Side.WHITE)

    def check_cell(self, x: int, y: int) -> None | Piece:
        return self.slots[x][y]

    def remove_piece(self, piece: Piece) -> None:
        self.slots[piece.x][piece.y] = None

    def move_piece(self, ):
        pass


