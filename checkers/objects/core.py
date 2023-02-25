from typing import List, Dict, Tuple

from checkers.objects.board import Board
from checkers.objects.piece import Piece


class Core:
    board: Board = Board()

    def __init__(self):
        pass

    def _validate_coords(self, x: int, y: int):
        return 0 <= x < len(self.board.slots[0]) and 0 <= y < len(self.board.slots)

    def get_moves(
            self, x: int, y: int, killed_so_far: List[List[int]], piece: Piece, prev_x: int, prev_y
    ) -> List[Dict[str, int]] | None:
        non_killing_moves = []
        killing_moves = []

        if piece.side.value == "white":
            i = -1
        else:
            i = 1
        for j in [-1, 1]:
            if not self._validate_coords(x + i, y + j):
                continue
            slot = self.board.check_cell(x + i, y + j)
            if b := slot is None:
                non_killing_moves.append({"x": x + i, "y": y + j, "kills": []})
            for i in [-1, 1]:
                if x + 2 * i == prev_x and y + 2 * j == prev_y:
                    continue
                if not b and slot.side != piece.side:
                    if self._validate_coords(x + 2 * i, y + 2 * j):
                        if self.board.check_cell(x + 2 * i, y + 2 * j) is None:
                            killed_so_far.append([x + i, y + j])
                            killing_moves += self.get_moves(
                                x + 2 * i, y + 2 * j, killed_so_far, piece, x, y
                            )
        if len(killing_moves) > 0:
            if prev_x != -1:
                [v["kills"].append([(x + prev_x) // 2, (y + prev_y) // 2]) for v in killing_moves]
            return killing_moves
        elif len(killed_so_far) > 0:
            return [{"x": x, "y": y, "kills": [[(x + prev_x) // 2, (y + prev_y) // 2]]}]
        elif non_killing_moves:
            return non_killing_moves
        return None
