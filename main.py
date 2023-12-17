import MainMenu
from games.tictactoeGame import tictactoe
from games.connect4 import connect4

menu = MainMenu.MainMenu()

menu.setTitle("Mini Games")

menu.addGame(tictactoe.TicTacToe("Tic Tac Toe"))
# menu.addGame(None)
menu.addGame(connect4.ConnectFour("Connect Four"))
menu.startMenuLoop()
