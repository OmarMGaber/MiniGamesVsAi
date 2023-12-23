class Minimax:
    @staticmethod
    def name():
        return "Minimax"

    def getMove(self, gameState):
        _, move = self.minimax(gameState, gameState.currentPlayer)
        return move

    def minimax(self, gameState, currentPlayer):
        winner = gameState.checkWin(gameState.board)
        if winner is not None and not winner == 0:
            if winner[0] == gameState.aiPlayer:
                return 1, None  # AI wins
            elif winner[0] == gameState.humanPlayer:
                return -1, None  # Human wins
        elif gameState.checkDraw(gameState.board):
            return 0, None  # Draw

        moves = gameState.getPossibleMoves()
        bestMove = None

        if currentPlayer == gameState.aiPlayer:
            bestScore = float('-inf')
            for move in moves:
                gameState.makeMove(gameState, move)
                score, _ = self.minimax(gameState, gameState.humanPlayer)
                gameState.undoMove(gameState, move)

                if score > bestScore:
                    bestScore = score
                    bestMove = move
        else:
            bestScore = float('inf')
            for move in moves:
                gameState.makeMove(gameState, move)
                score, _ = self.minimax(gameState, gameState.aiPlayer)
                gameState.undoMove(gameState, move)

                if score < bestScore:
                    bestScore = score
                    bestMove = move

        return bestScore, bestMove
