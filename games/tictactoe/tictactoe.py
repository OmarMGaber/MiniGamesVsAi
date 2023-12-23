from games import smartGame
import utilities as util

import algorithms.minimax


class TicTacToe(smartGame.SmartGame):
    emptySpotChar = " "
    player1, player2 = 'X', 'O'

    def __init__(self, title):
        super().__init__(title)
        self.boardSideLength = 3
        self.board = [[TicTacToe.emptySpotChar for _ in range(self.boardSideLength)] for _ in
                      range(self.boardSideLength)]
        self.currentPlayer = "X"
        self.humanPlayer = None
        self.aiPlayer = None
        self.isVsAI, self.aiAlgorithm = False, None

    def getTitle(self):
        return self.title

    def vsAI(self, aiAlgorithm, aiTurn):
        self.setAiAlgorithm(aiAlgorithm)
        self.setAiTurn(aiTurn)

    def setAiAlgorithm(self, aiAlgorithm):
        self.aiAlgorithm = aiAlgorithm
        self.isVsAI = True
        if self.aiPlayer is None:
            self.aiPlayer = self.player2

    def setAiTurn(self, num):
        if self.aiAlgorithm is None:
            raise Exception("AI Algorithm not set")
        if num == 1:
            self.aiPlayer = self.player1
            self.humanPlayer = self.player2
        elif num == 2:
            self.aiPlayer = self.player2
            self.humanPlayer = self.player1

    @staticmethod
    def printBoard(board, tab=0):
        i = 0
        print("\t" * tab, " ====Board====")
        for row in board:
            print("\t" * tab, ' | ', end='')
            for col in row:
                if col == TicTacToe.emptySpotChar:
                    print(i + 1, end=' | ')
                else:
                    print(col, end=' | ')
                i += 1

            print()  # newline
            if i != 9:
                print("\t" * tab, " -------------")

        print("\t" * tab, " =============\n")

    @staticmethod
    def undoMove(gameState, move):
        gameState.board[move[0]][move[1]] = TicTacToe.emptySpotChar
        gameState.switchTurn()

    @staticmethod
    def checkWin(board):
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] != TicTacToe.emptySpotChar:
                return row[0]

        # Check columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] != TicTacToe.emptySpotChar:
                return board[0][i]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != TicTacToe.emptySpotChar:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != TicTacToe.emptySpotChar:
            return board[0][2]

        return None

    @staticmethod
    def checkDraw(board):
        for row in board:
            for col in row:
                if col == TicTacToe.emptySpotChar:
                    return False
        return True

    def switchTurn(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    def getPossibleMoves(self):
        moves = []
        for row in range(self.boardSideLength):
            for col in range(self.boardSideLength):
                if self.board[row][col] == TicTacToe.emptySpotChar:
                    moves.append((row, col))
        return moves

    def checkMove(self, move):
        if move[0] < 0 or move[0] > self.boardSideLength - 1 or move[1] < 0 or move[1] > self.boardSideLength - 1:
            return False
        if self.board[move[0]][move[1]] == TicTacToe.emptySpotChar:
            return True
        else:
            return False

    @staticmethod
    def makeMove(gameState, move):
        gameState.board[move[0]][move[1]] = gameState.currentPlayer
        gameState.switchTurn()

    def getPlayerMove(self):
        print("Player " + self.currentPlayer + "'s turn")
        move = None
        while True:
            try:
                move = int(input("Enter a valid move (1-9): "))
                if move < 1 or move > 9:
                    print("Invalid input")
                    continue
                move -= 1
                if self.checkMove((move // 3, move % 3)):
                    break
                else:
                    print("Invalid move")
            except ValueError:
                print("Invalid input")

        return move // 3, move % 3

    @staticmethod
    def isEmptySpot(board, row, col):
        return board[row][col] == TicTacToe.emptySpotChar

    @staticmethod
    def printWinnerPrompt(game, winner):
        if winner == game.player1:
            if game.isVsAI and game.aiPlayer == game.player1:
                print("AI wins!")
            else:
                print("Player X wins!")
        else:
            if game.isVsAI and game.aiPlayer == game.player2:
                print("AI wins!")
            else:
                print("Player O wins!")

    # @staticmethod
    def getGameSettingsFromUser(self):
        print("Do you want to play against AI? (y/n)")
        userChoice = util.getAndValidateUserInput(["y", "n", "Y", "N"], "Enter your choice: ",
                                                  "Invalid choice. Please try again.")
        if userChoice.lower() == "y":
            print("Playing against AI.")
            self.setAiAlgorithm(algorithms.minimax.Minimax())
            print("AI Algorithms: " + self.aiAlgorithm.name())

            print("Choose your turn: ")
            print("1: X")
            print("2: O")
            userChoice = util.getAndValidateUserInput(["1", "2"], "Enter your choice: ",
                                                      "Invalid choice. Please try again.")
            if userChoice == "1":
                self.setAiTurn(2)
            else:
                self.setAiTurn(1)

        else:
            print("Playing against human.")

    def printGameSettings(self):
        print("\nGame Settings:")

        if self.isVsAI:
            print("\tPlaying against AI")
            print("\tAI Algorithm: " + self.aiAlgorithm.name())
            print("\tAI Turn: " + self.aiPlayer)
        else:
            print("\tPlaying against human")

        print("\tPlayer 1: " + self.player1)
        print("\tPlayer 2: " + self.player2)
        print("\tCurrent Turn: " + self.currentPlayer)
        print("\tBoard: ")
        self.printBoard(self.board, 2)
        input("\nPress any key to start playing...")

    def startGame(self):

        print("Welcome to Tic Tac Toe!\n")
        self.getGameSettingsFromUser()
        self.printGameSettings()

        while True:
            if self.isVsAI and self.currentPlayer == self.aiPlayer:
                move = self.aiAlgorithm.getMove(self)
                self.makeMove(self, move)
            else:
                self.printBoard(self.board)

                move = self.getPlayerMove()
                self.makeMove(self, move)

            winner = self.checkWin(self.board)
            if winner is not None:
                self.printBoard(self.board)
                self.printWinnerPrompt(self, winner)
                break

            if self.checkDraw(self.board):
                self.printBoard(self.board)
                print("Draw!")
                break


# for testing
if __name__ == "__main__":
    game = TicTacToe("Tic Tac Toe")
    game.startGame()
