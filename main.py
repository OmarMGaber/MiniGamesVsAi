import MainMenu
from games.tictactoe import tictactoe
from games.connect4 import connect4
from games.mazeSolver import maze
from games.EightPuzzleGame import eight_puzzle

menu = MainMenu.MainMenu("Mini Games")

menu.addGame(tictactoe.TicTacToe("Tic Tac Toe"))
menu.addGame(eight_puzzle.EightPuzzle("Eight Puzzle"))
menu.addGame(connect4.ConnectFour("Connect Four"))
menu.addGame(maze.Maze("Maze Solver"))

menu.startMenuLoop()
