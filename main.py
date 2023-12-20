import MainMenu
from games.tictactoe import tictactoe
from games.connect4 import connect4
from games.mazeSolver import maze

menu = MainMenu.MainMenu()

menu.setTitle("Mini Games")

menu.addGame(tictactoe.TicTacToe("Tic Tac Toe"))
# menu.addGame(None)
menu.addGame(connect4.ConnectFour("Connect Four"))
menu.addGame(maze.Maze("Maze Solver"))
menu.startMenuLoop()
