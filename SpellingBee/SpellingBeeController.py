import SpellingBeeModel

class SpellingBeeController:
    def __init__(self):
        self.__wordleModel = SpellingBeeModel.SpellingBeeModel()



    #Refresh game 
    def refreshGame(self):
        self.__wordleModel.clearAnswerList()
        self.__wordleModel.resetPoints()
        self.__wordleModel.generateUsableLetters()

    def getInvalidLetters(self):
        return self.__wordleModel.getInvalidLetters()

    def getUsableLetters(self):
        return self.__wordleModel.getUsableLetters()

    def processInput(self, userInput):
        if not self.__wordleModel.hasValidLetters():
            return False
        elif not self.__wordleModel.containsWord(userInput):
            return False
        else:
            self.__wordleModel.addValidAnswer(userInput)
            self.__wordleModel.addPoint()
            return True

    #gets the list of words that user input
    def getUserAnswers(self):
        return self.getUserAnswers()

    def getGamePoints(self):
        return self.__wordleModel.getPoints()

