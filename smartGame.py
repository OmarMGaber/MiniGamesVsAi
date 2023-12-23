from abc import ABC, abstractmethod

from games.miniGame import MiniGame


class SmartGame(MiniGame, ABC):
    """ SmartGame is an abstract class that all games that use AI must inherit from. """

    def __init__(self, title):
        super().__init__(title)
        self.isVsAI = False
        self.aiAlgorithm = None
        self.aiPlayer = None
        self.humanPlayer = None

    @abstractmethod
    def vsAI(self, aiAlgorithm, aiTurn):
        pass

    @abstractmethod
    def setAiAlgorithm(self, aiAlgorithm):
        pass

    @abstractmethod
    def setAiTurn(self, num):
        pass

    @staticmethod
    @abstractmethod
    def getPossibleMoves(gameState):
        pass

    @staticmethod
    @abstractmethod
    def makeMove(gameState, move):
        pass

    @staticmethod
    @abstractmethod
    def undoMove(gameState, move):
        pass
