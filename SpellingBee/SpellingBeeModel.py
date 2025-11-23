import WordRepository.DictionaryReader as reader
import random

class SpellingBeeModel:

    def __init__(self):
        self.__points = 0 
        self.__validAnswers = []
        self.__validLetters = ""
        WordListGenerator = reader.WordDictionary("WordRepository\words_dictionary.json")
        self.__wordList = WordListGenerator.getWordsOfLength(7)
        self.generateValidLetters(self)

    #checks to see if userInput contains the 7 selected words

    #Generates list of 7 random characters, at least two to three vowels and 5 constants
    def generateValidLetters(self):
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        maxInput = 7
        chosenVowelCount = random.randint(1,3)
        chosenConsonantCount = maxInput - chosenVowelCount
        newValidAnswers = []
        for x in range(chosenVowelCount):
            newValidAnswers.append(vowels[random.randint(len(vowels)-1)])
        for x in range(chosenConsonantCount):
            newValidAnswers.append(consonants[random.randint(len(consonants)-1)])
            
    def hasValidLetters(self, userInput):
        userInput = list(userInput)
        for letter in userInput:
            if letter not in self.__validLetters:
                return False
        return True
    #gets list of letter that are invalid to respond to user
    def getInvalidLetters(self,userInput):
        userInput = str(list(userInput))
        invalidLetterList = []
        for letter in userInput:
            if letter not in self.__validLetters:
                invalidLetterList.append[letter]
        invalidLetterList
        
    #If word found in list of words length 7, return true
    def containsWord(self, userInput):
        if userInput in self.__wordList:
            return False
        else:
            return True
    def addPoint(self):
        self.__points += 1
    def getPoints(self):
        return self.__points
    def resetPoints(self):
        self.__points = 0
    def getValidAnswers(self):
        return self.__validAnswers
    def addValidAnswer(self, str):
        self.__validAnswers.append(str)
        return True
    def clearAnswerList(self):
        self.__validAnswers = []








