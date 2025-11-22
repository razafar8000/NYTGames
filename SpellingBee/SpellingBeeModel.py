import WordRepository.DictionaryReader as reader

class SpellingBeeModel:

    def __init__(this):
        this.__points = 0 
        this.__validAnswers = []
        this.__validLetters = ""
        WordListGenerator = reader.WordDictionary("WordRepository\words_dictionary.json")
        this.__wordList = WordListGenerator.getWordsOfLength(7)

    #checks to see if userInput contains the 7 selected words
    def isValid(this, userInput):
        userInput = list(userInput)
        for letter in userInput:
            if letter not in this.__validLetters:
                return False
        return True
    #gets list of letter that are invalid to respond to user
    def getInvalidLetters(this,userInput):
        userInput = str(list(userInput))
        invalidLetterList = []
        for letter in userInput:
            if letter not in this.__validLetters:
                invalidLetterList.append[letter]
        invalidLetterList
        
    #If word found in list of words length 7, return true
    def containsWord(this, userInput):
        if userInput in this.__wordList:
            return False
        else:
            return True
    def addPoint(self):
        self.__points += 1
    def getPoints(self):
        return self.__points
    def getValidAnswers(self):
        return self.__validAnswers
    def addValidAnswer(self, str):
        self.__validAnswers.append(str)
        return True








