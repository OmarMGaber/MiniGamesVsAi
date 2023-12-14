import MainMenu
from games.tictactoeGame import TicTacToe

menu = MainMenu.MainMenu()

menu.setTitle("Mini Games")

menu.addGame(TicTacToe.TicTacToe("Tic Tac Toe"))
# menu.addGame(None)

menu.startMenuLoop()
