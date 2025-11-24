from wordle.RandomWordFetcher import *
from wordle.Guess import Guess

'''
WordleModel Class
    - tracks:
        - num of guesses made
        - game score
        - Guess Objects for made guesses (guessesMade list)
    - holds secret word
    - can check and change game states (WIN/LOSS/RESET)
'''

class WordleModel:
    def __init__(self):
        self.__guessCount = 0
        self.__gameScore = 0
        self.__guessesMade = [None] * 6

        #random word
        secString = fetchWord()
        if secString is not None:
            self.__secretWord = secString.lower()
        else:
            self.__secretWord = "apple" #default

    #store new guess object and increment guessCount
    def makeGuess(self, guess:str):
        if self.__guessCount < 6:
            userGuess = Guess(guess.lower(), self.__secretWord)
            self.__guessesMade[self.__guessCount] = userGuess
            self.__guessCount += 1

    #continuous play - reset guesses and new word
    def resetGame(self):
        self.__guessCount = 0
        self.__guessesMade.clear()

        secString = fetchWord()
        if secString is not None:
            self.__secretWord = secString.lower()
        else:
            self.__secretWord = "apple"  # default


    #Win/Loss Check
    def isWon(self)->bool:
        if self.__guessCount==0:
            return False
        else:
            return self.__guessesMade[self.__guessCount-1].getGuess() == self.__secretWord and self.__guessCount <= 6

    def isLost(self)->bool:
        if self.__guessCount==0:
            return False
        else:
            return self.__guessCount == 6 and not self.__guessesMade[self.__guessCount-1].getGuess() == self.__secretWord


    #GETTERS/SETTERS
    def getSecretWord(self)->str:
        return self.__secretWord
    def getGuesses(self):
        return self.__guessesMade
    def getGuessCount(self):
        return self.__guessCount
    def incrementGameScore(self):
        self.__gameScore += 1
    def getGameScore(self):
        return self.__gameScore

