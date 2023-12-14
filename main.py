from MainMenu import MainMenu
from MiniGamesAI.games.tictactoeGame import TicTacToe

menu = MainMenu()

menu.setTitle("Mini Games")

# menu.addGame(TicTacToe.TicTacToe("Tic Tac Toe"))
menu.addGame(None)

menu.startMenuLoop()
