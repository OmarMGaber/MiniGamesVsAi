import tkinter as tk
from games.miniGame import MiniGame
from utilities import getAndValidateUserInput


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
        self.isGameOver = False

    def getTitle(self):
        return self.title

    # Debugging method
    def printBoard(self):
        for row in self.board:
            print(row)

        print()

    @staticmethod
    def makeMove(board, column, currentPlayer):
        i = ConnectFour.findNextEmptySpot(board, column)

        if i == -1:
            return False

        board[i - 1][column] = currentPlayer
        return True

    @staticmethod
    def findNextEmptySpot(board, column):
        """ Returns the row number of the next empty spot in the column, or False if the column is full or invalid """

        if column < 0 or column > 6:
            return -1

        if board[0][column] != 0:
            return -1

        i = 0
        while i != 6 and board[i][column] == 0:
            i += 1

        return i

    def switchTurn(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    @staticmethod
    def checkWin(board):
        """ Returns 0 if no one has won, otherwise returns the player who won and the winning pieces """

        # check horizontal
        for row in board:
            for i in range(4):
                if row[i] == row[i + 1] == row[i + 2] == row[i + 3] != 0:
                    return row[i], [(board.index(row), i), (board.index(row), i + 1), (board.index(row), i + 2),
                                    (board.index(row), i + 3)]

        # check vertical
        for i in range(7):
            for j in range(3):
                if board[j][i] == board[j + 1][i] == board[j + 2][i] == board[j + 3][i] != 0:
                    return board[j][i], [(j, i), (j + 1, i), (j + 2, i), (j + 3, i)]

        # check diagonal
        for i in range(3):
            for j in range(4):
                if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] != 0:
                    return board[i][j], [(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)]

        for i in range(3, 6):
            for j in range(4):
                if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2] == board[i - 3][j + 3] != 0:
                    return board[i][j], [(i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)]

        return 0

    def checkDraw(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True

    def showBoard(self):
        print("============Board============")
        print("  1   2   3   4   5   6   7")
        for row in self.board:
            print("|", end="")
            for col in row:
                if col == 0:
                    print("  ", end="")
                elif col == ConnectFour.RED_TURN:
                    print(" R", end="")
                elif col == ConnectFour.YELLOW_TURN:
                    print(" Y", end="")
                print(" |", end="")
            print()
        print("=============================")

    def resetGame(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.currentPlayer = self.player1
        self.isGameOver = False

    def startGUI(self):
        root = tk.Tk()
        width = 900
        height = 900
        root.title(self.title)
        root.geometry(str(width) + "x" + str(height))
        root.resizable(False, False)

        canvas = tk.Canvas(root, width=width, height=height, bg="light gray", bd=0, highlightthickness=0)
        canvas.pack()

        def resetGame():
            self.resetGame()
            drawBoard()
            updateCurrentPlayerColor()
            updateStatusLabel("Playing")
            showResetButton(False)

        # add reset button
        resetButton = tk.Button(root, text="Reset", font=("Arial", 20), command=resetGame)

        title = tk.Label(root, text=self.title, font=("Arial", 30))

        currentPlayerLabel = tk.Label(root, text="Current player:", font=("Arial", 20), fg="black")
        playerColor = tk.Label(root, text="Red", font=("Arial", 20), fg="red")

        statusLabel = tk.Label(root, text="Status:", font=("Arial", 20), fg="black")
        currentStatusLabel = tk.Label(root, text="Playing", font=("Arial", 20), fg="black")

        title.place(x=width / 2, y=50, anchor="center")

        currentPlayerLabel.place(x=100, y=800)
        playerColor.place(x=300, y=800)

        statusLabel.place(x=100, y=850)
        currentStatusLabel.place(x=300, y=850)

        def showResetButton(show):
            if show:
                resetButton.place(x=750, y=800)
            else:
                resetButton.place_forget()

        def updateCurrentPlayerColor():
            if self.currentPlayer == ConnectFour.RED_TURN:
                playerColor.config(text="Red", fg="red")
            elif self.currentPlayer == ConnectFour.YELLOW_TURN:
                playerColor.config(text="Yellow", fg="yellow")

        def drawBoard():
            for i in range(6):
                for j in range(7):
                    canvas.create_rectangle(100 + 100 * j, 100 + 100 * i, 200 + 100 * j, 200 + 100 * i, fill="white",
                                            outline="black")
                    if self.board[i][j] == ConnectFour.RED_TURN:
                        canvas.create_oval(100 + 100 * j, 100 + 100 * i, 200 + 100 * j, 200 + 100 * i, fill="red",
                                           outline="black")
                    elif self.board[i][j] == ConnectFour.YELLOW_TURN:
                        canvas.create_oval(100 + 100 * j, 100 + 100 * i, 200 + 100 * j, 200 + 100 * i, fill="yellow",
                                           outline="black")

        def markWinner(winner):
            # draw a line through the winning pieces
            canvas.create_line(150 + 100 * winner[0][1], 150 + 100 * winner[0][0], 150 + 100 * winner[3][1],
                               150 + 100 * winner[3][0], fill="black", width=5)

        def updateStatusLabel(message, fg="black"):
            currentStatusLabel.config(text=message, fg=fg)

        def eventHandler(e):
            if self.isGameOver:
                showResetButton(True)
                return
            else:
                showResetButton(False)

            x = e.x
            y = e.y

            if x < 100 or x > 800 or y < 100 or y > 700:
                return

            column = (x - 100) // 100

            if not self.makeMove(self.board, column, self.currentPlayer):
                updateStatusLabel("Invalid move")
            else:
                updateStatusLabel("Playing")
                updateCurrentPlayerColor()
                drawBoard()

                winner = ConnectFour.checkWin(self.board)
                if winner != 0:
                    self.isGameOver = True
                    showResetButton(True)

                    if winner[0] == ConnectFour.RED_TURN:
                        updateStatusLabel("Red wins", fg="red")
                    else:
                        updateStatusLabel("Yellow wins", fg="yellow")

                    markWinner(winner[1])
                    return

                if self.checkDraw():
                    showResetButton(True)
                    self.isGameOver = True
                    updateStatusLabel("Draw")
                    return

                self.switchTurn()
                updateCurrentPlayerColor()

        root.bind('<Button-1>', eventHandler)
        drawBoard()
        root.mainloop()

    def startConsole(self):
        while True:
            self.showBoard()

            if self.isGameOver:
                print("Game over")
                break

            print("Current player: ", end="")
            if self.currentPlayer == ConnectFour.RED_TURN:
                print("Red")
            elif self.currentPlayer == ConnectFour.YELLOW_TURN:
                print("Yellow")

            move = int(getAndValidateUserInput([str(i + 1) for i in range(7)], "Enter a valid move (1-7): ",
                                           "Invalid move. Please try again.")) - 1

            if not self.makeMove(self.board, move, self.currentPlayer):
                print("Invalid move")
                continue

            winner = ConnectFour.checkWin(self.board)
            if winner != 0:
                self.showBoard()
                if winner[0] == ConnectFour.RED_TURN:
                    print("Red wins")
                else:
                    print("Yellow wins")
                break

            if self.checkDraw():
                self.showBoard()
                print("Draw")
                break

            self.switchTurn()

    def startGame(self):
        self.startGUI()

c4 = ConnectFour("Connect Four")
# c4.startGame()
c4.startConsole()