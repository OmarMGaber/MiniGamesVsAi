def getAndValidateUserInput(listOfChoices, inputMessage, errorMessage):
    while True:
        try:
            userInput = input(inputMessage)
            if userInput in listOfChoices:
                return userInput
            else:
                print('\t', errorMessage)
        except ValueError:
            print('\t', errorMessage)
