import unittest

from checkers.objects.core import Core
from checkers.objects.piece import Piece, Side


class TestCore(unittest.TestCase):

    def test_get_moves(self):
        core = Core()
        # for i in range(8):
        #     for j in range(8):
        core.board.slots[3][2] = Piece(3, 2, Side.WHITE)
        core.board.slots[6][1] = None
        core.board.slots[6][5] = None
        print(core.board.check_cell(2, 1))
        print(core.get_moves(2, 1, [], core.board.check_cell(2, 1), -1, -1))

