import SpellingBeeModel

class SpellingBeeController:
    def __init__(self):
        self.__buffer = ""
        self.__wordleModel = SpellingBeeModel.SpellingBeeModel()
        self.__guessState = False



    #Refresh game 
    def refreshGame(self):
        self.__wordleModel.clearAnswerList()
        self.__wordleModel.resetPoints()
        self.__wordleModel.generateValidLetters()
        self.resetBuffer()

    #copied from WordleController, Process user input, passes it on to the function processGuess when finished
    def onKeyPress(self, key:str):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if len(self.__buffer)<=7:
            if (key == "ENTER" and len(self.__buffer)<=7): #valid guess entered
                self.onGuess(self.__buffer)
                self.__guessState = self.processBuffer(self.__buffer)
                self.resetBuffer()
            elif key=="BACKSPACE" and len(self.__buffer)>0: #backspace pressed - decrement guess buffer
                self.__buffer=self.__buffer[:-1]
            elif len(key)==1 and key.isalpha() and len(self.__buffer)<=7: #key pressed - add to guess buffer
                self.__buffer=self.__buffer+key.lower()
    

    def processBuffer(self,buffer):
        if not self.__wordleModel.hasValidLetters():
            return False
        elif not self.__wordleModel.containsWord(buffer):
            return False
        else:
            self.__wordleModel.addValidAnswer(buffer)
            self.__wordleModel.addPoint()
            return True

    def setBuffer(self, str):
        self.__buffer = str

    def getBuffer(self):
        return self.__buffer

    def getGamePoints(self):
        return self.__wordleModel.getPoints()

    def resetBuffer(self):
        self.__buffer = ""
    
    def resetGuessState(self):
        self.__guessState = False
    