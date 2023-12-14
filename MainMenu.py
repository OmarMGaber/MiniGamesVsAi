import os
from time import sleep

from utilities import getAndValidateUserInput


class MainMenu:
    def __init__(self):
        self.gamesArray = []
        self.title = "Mini Games"

    def setTitle(self, newTitle):
        if newTitle is None:
            raise Exception("Title cannot be None")

        self.title = newTitle

    def addGame(self, gameObject):
        """" Game object must have a title and a startGame method. """
        if gameObject is None:
            raise Exception("Game object cannot be None")

        self.gamesArray.append(gameObject)

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

        print("\t", str(len(self.gamesArray) + 1) + ": Exit")
        print()
        return True

    def showMenu(self):
        print("==== " + self.title + " ====")
        if not self.showGames():
            return False

        userChoice = int(getAndValidateUserInput([str(i + 1) for i in range(len(self.gamesArray) + 1)],
                                                 "Enter your choice: ", "Invalid choice. Please try again."))

        if userChoice == len(self.gamesArray) + 1:
            return None
        try:
            print("You chose: " + self.gamesArray[userChoice - 1].getTitle())
            print("Starting game...")
            print("\n\n")
            sleep(1)  # wait for 1 second to let the user read the message
            
            self.gamesArray[userChoice - 1].startGame()
        except AttributeError:
            print("Game " + str(userChoice) + " has no startGame method.")
            return False

        return True

    def startMenuLoop(self):
        while True:
            # clear screen and show menu
            os.system("cls")

            menuFlag = self.showMenu()  # returns None if user chose to exit, False if user chose to go back to main menu, True if user chose to play a game
            if menuFlag is None:
                print("Exiting...")
                break
            elif not menuFlag:
                break

            print("Do you want to play another game? (y/n)")
            userChoice = getAndValidateUserInput(["y", "n", "Y", "N"],
                                                 "Enter your choice: ",
                                                 "Invalid choice. Please try again.")
            if userChoice.lower() == "n":
                break
