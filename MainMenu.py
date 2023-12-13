class MainMenu:
    def __init__(self):
        self.gamesArray = []
        self.title = "Mini Games"

    def setTitle(self, newTitle):
        if newTitle is not None:
            self.title = newTitle
            return True

        return False

    def addGame(self, gameObject):
        """" Game object must have a title and a startGame method. """
        if gameObject is not None:
            self.gamesArray.append(gameObject)
            return True

        return False

    def showGames(self):
        if len(self.gamesArray) == 0:
            print("No games found.")
            return False

        print("Choose a game: ")
        for i in range(len(self.gamesArray)):
            print(str(i) + ": " + self.gamesArray[i].title)

        return True

    @staticmethod
    def getAndValidateUserChoice(upperLimit, lowerLimit=0):
        while True:
            try:
                userChoice = int(input("Enter your choice: "))
                if lowerLimit <= userChoice <= upperLimit:
                    return userChoice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid choice. Please try again.")

    def showMenu(self):
        print(self.title)
        ret = self.showGames()
        if not ret:
            return False
        userChoice = self.getAndValidateUserChoice(len(self.gamesArray) - 1)
        print("You chose: " + self.gamesArray[userChoice].title + ". Starting game...")
        self.gamesArray[userChoice].startGame()

    def startMenuLoop(self):
        while True:
            ret = self.showMenu()
            if not ret:
                break
            print("Do you want to play another game?")
            userChoice = self.getAndValidateUserChoice(1, 0)
            if userChoice == 0:
                break
