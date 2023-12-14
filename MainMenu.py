import os
from time import sleep

from MiniGamesAI.utilities import getAndValidateUserInput


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
            try:
                print("\t", str(i + 1) + ": " + self.gamesArray[i].getTitle())
            except AttributeError:
                print("Game " + str(i + 1) + " has no title.")

        print()
        return True

    def showMenu(self):
        print("==== " + self.title + " ====")
        if not self.showGames():
            return False

        userChoice = int(getAndValidateUserInput([str(i + 1) for i in range(len(self.gamesArray))],
                                                 "Enter your choice: ", "Invalid choice. Please try again."))

        print("You chose: " + self.gamesArray[userChoice - 1].getTitle())
        print("Starting game...")
        print("\n\n")
        sleep(1)

        try:
            self.gamesArray[userChoice - 1].startGame()
        except AttributeError:
            print("Game " + str(userChoice) + " has no startGame method.")
            return False

        return True

    def startMenuLoop(self):
        while True:

            if not self.showMenu():
                break

            print("Do you want to play another game? (y/n)")
            userChoice = getAndValidateUserInput(["y", "n", "Y", "N"],
                                                 "Enter your choice: ",
                                                 "Invalid choice. Please try again.")
            if userChoice == 0:
                break

            # clear the screen if the user
            os.system('cls' if os.name == 'nt' else 'clear')
