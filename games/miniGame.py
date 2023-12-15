from abc import abstractmethod, ABC


# Mini Game class is an abstract class that all games must inherit from.
class MiniGame(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def getTitle(self):
        return self.title

    @abstractmethod
    def startGame(self):
        raise NotImplementedError("Subclasses must implement the startGame method")
