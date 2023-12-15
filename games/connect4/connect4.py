from abc import ABC

from games.miniGame import MiniGame


class ConnectFour(MiniGame):
    RED_TURN = 1
    YELLOW_TURN = 2

    def __init__(self, title):
        super().__init__(title)
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.title = title
        self.player1 = ConnectFour.RED_TURN
        self.player2 = ConnectFour.YELLOW_TURN
        self.currentPlayer = self.player1

    def getTitle(self):
        return self.title

    def checkWinner(self):
        for i in range(6):
            for j in range(7):
                if self.board[i][j] != 0:
                    if self.checkVertical(i, j) or self.checkHorizontal(i, j) or self.checkDiagonal(i, j):
                        return True

        return False


    def startGame(self):
        pass
