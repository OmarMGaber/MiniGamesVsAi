import os
from time import sleep

from utilities import getAndValidateUserInput


class MainMenu:
    EXIT_FLAG = 0
    NO_GAMES_FOUND_FLAG = -1


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
            return MainMenu.NO_GAMES_FOUND_FLAG

        userChoice = int(getAndValidateUserInput([str(i + 1) for i in range(len(self.gamesArray) + 1)],
                                                 "Enter your choice: ", "Invalid choice. Please try again."))

        if userChoice == len(self.gamesArray) + 1:
            return MainMenu.EXIT_FLAG
        try:
            print("You chose: " + self.gamesArray[userChoice - 1].getTitle())
            print("Starting game...")
            print("\n\n")
            sleep(1)  # wait for 1 second to let the user read the message
            os.system("cls")

            self.gamesArray[userChoice - 1].startGame()
            # reset the game to its initial state after it finishes
            self.gamesArray[userChoice - 1].__init__(self.gamesArray[userChoice - 1].getTitle())

            print("Press q to go back to the menu.")
            while input().lower() != "q":
                pass
            os.system("cls")

        except AttributeError:
            raise Exception("Game " + str(userChoice) + " has no startGame method.")

        return True

    def startMenuLoop(self):
        while True:
            # clear screen and show menu
            os.system("cls")

            menuFlag = self.showMenu()
            if menuFlag is MainMenu.EXIT_FLAG:
                print("Exiting...")
                exit(MainMenu.EXIT_FLAG)

            elif menuFlag is MainMenu.NO_GAMES_FOUND_FLAG:
                exit(MainMenu.NO_GAMES_FOUND_FLAG)

            print("Do you want to play another game? (y/n)")
            userChoice = getAndValidateUserInput(["y", "n", "Y", "N"],
                                                 "Enter your choice: ",
                                                 "Invalid choice. Please try again.")
            if userChoice.lower() == "n":
                break
