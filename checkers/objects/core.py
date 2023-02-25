from typing import List, Dict

from checkers.objects.board import Board
from checkers.objects.piece import Piece


class Core:
    board: Board = Board()

    def __init__(self):
        pass

    def _validate_coords(self, x: int, y: int):
        return 0 <= x < len(self.board.slots[0]) and 0 <= y < len(self.board.slots)

    def get_moves(self, x: int, y: int) -> List[Dict[str, int]]:
        # moves = self._check_around()
        pass

    def _check_around(self, x: int, y: int, killed_so_far: int, piece: Piece, prev_x: int, prev_y):
        non_killing_moves = []
        killing_moves = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                if x + 2 * i == prev_x and y + 2 * j == prev_y:
                    continue
                if not self._validate_coords(x + i, y + j):
                    continue
                slot = self.board.check_cell(x + i, y + j)
                if slot is None:
                    non_killing_moves.append({"x": x + i, "y": y + j, "kill-count": 0})
                elif slot.side != piece.side:
                    if self._validate_coords(x + 2 * i, y + 2 * j):
                        if self.board.check_cell(x + 2 * i, y + 2 * j) is None:
                            killing_moves += self._check_around(x + 2 * i, y + 2 * j, killed_so_far + 1, piece, x, y)
        if len(killing_moves) > 0:
            return killing_moves
        elif killed_so_far > 0:
            return [{"x": x, "y": y, "kill-count": killed_so_far}]
        elif non_killing_moves:
            return non_killing_moves
        else:
            return None











