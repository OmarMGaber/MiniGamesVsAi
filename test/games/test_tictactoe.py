import unittest
from unittest.mock import patch
from io import StringIO
from games.tictactoe.tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe("Tic Tac Toe")

    def test_check_move_valid(self):
        valid_moves = [(0, 0), (1, 1), (2, 2)]
        for move in valid_moves:
            result = self.game.checkMove(move)
            self.assertTrue(result)

    def test_check_move_invalid(self):
        invalid_moves = [(-1, 0), (0, -1), (3, 0), (0, 3)]
        for move in invalid_moves:
            result = self.game.checkMove(move)
            self.assertFalse(result)

    def test_make_move(self):
        move = (0, 0)
        self.game.makeMove(move)
        self.assertEqual(self.game.board[0][0], self.game.currentPlayer)

    def test_switch_turn(self):
        initial_turn = self.game.currentPlayer
        self.game.switchTurn()
        self.assertNotEqual(self.game.currentPlayer, initial_turn)

    def test_check_win_horizontal(self):
        self.game.board = [['X', 'X', 'X'], [' ', 'O', 'O'], [' ', ' ', ' ']]
        winner = self.game.checkWin(self.game.board)
        self.assertEqual(winner, 'X')

    def test_check_win_vertical(self):
        self.game.board = [['X', 'O', 'O'], ['X', 'O', 'X'], ['X', ' ', ' ']]
        winner = self.game.checkWin(self.game.board)
        self.assertEqual(winner, 'X')

    def test_check_win_diagonal(self):
        self.game.board = [['X', 'O', 'O'], [' ', 'X', 'X'], ['O', ' ', 'X']]
        winner = self.game.checkWin(self.game.board)
        self.assertEqual(winner, 'X')

    def test_check_draw(self):
        self.game.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        result = self.game.checkDraw(self.game.board)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
