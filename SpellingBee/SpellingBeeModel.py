import WordRepository.DictionaryReader as reader
import random

class SpellingBeeModel:

    def __init__(self):
        self.__points = 0 
        self.__validAnswers = []
        self.__usableLetters = self.generateUsableLetters()
        self.__wordList = reader.WordDictionary("WordRepository\words_dictionary.json")

    #checks to see if userInput contains the 7 selected words

    #creates a random list of 7 characters that contains letters that are able to be used in spelling bee

    def getUsableLetters(self):
        return self.__usableLetters

    def generateUsableLetters(self):
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        maxInput = 7

        chosenVowelCount = random.randint(1,3)
        chosenConsonantCount = maxInput - chosenVowelCount
        newUsableLetters = ""

        #chooses random index in vowels and consonant string
        for x in range(chosenVowelCount):
            randomIndex = random.randint(len(vowels)-1)
            newUsableLetters += vowels[randomIndex]
        for x in range(chosenConsonantCount):
            randomIndex = random.randint(len(vowels)-1)
            newUsableLetters += consonants[randomIndex]

        self.__usableLetters = newUsableLetters
        return newUsableLetters
    

    def hasValidLetters(self, userInput):
        userInput = list(userInput)
        for letter in userInput:
            if letter not in self.__usableLetters:
                return False
        return True
    
    #gets list of letter that are invalid to input (for UI purposes)
    def getInvalidLetters(self, buffer):
        bufferList = str(list(buffer))
        invalidLetterList = []
        for letter in bufferList:
            if letter not in self.__usableLetters:
                invalidLetterList.append[letter]
        return invalidLetterList
        
    #If word found in list of words length 7, return true
    def containsWord(self, userInput):
        return self.__wordList.contains(userInput)

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








