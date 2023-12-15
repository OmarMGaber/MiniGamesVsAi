import mainMenu
from games.tictactoeGame import tictactoe

menu = MainMenu.MainMenu()

menu.setTitle("Mini Games")

menu.addGame(TicTacToe.TicTacToe("Tic Tac Toe"))
# menu.addGame(None)

menu.startMenuLoop()
