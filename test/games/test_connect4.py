import unittest
from games.connect4 import connect4


class TestConnect4(unittest.TestCase):

    def setUp(self):
        self.game = connect4.ConnectFour("Connect Four")

    def test_findNextEmptySpot_valid(self):
        valid_moves = [0, 1, 2, 3, 4, 5, 6]
        for move in valid_moves:
            result = self.game.findNextEmptySpot(self.game.board, move)
            self.assertTrue(result)

    def test_findNextEmptySpot_invalid(self):
        invalid_moves = [-1, 7]
        for move in invalid_moves:
            result = self.game.findNextEmptySpot(self.game.board, move)
            self.assertEqual(result, -1)

    def test_make_move(self):
        move = 0
        self.game.makeMove(self.game.board, move, self.game.currentPlayer)
        self.assertEqual(self.game.board[5][0], self.game.currentPlayer)

    def test_switch_turn(self):
        initial_turn = self.game.currentPlayer
        self.game.switchTurn()
        self.assertNotEqual(self.game.currentPlayer, initial_turn)


if __name__ == '__main__':
    unittest.main()
