from wordle import WordleModel
import requests
import os

'''
UI INTEGRATION GUIDE (remove when finished):
    1. py file for UI should only need a WordleController object
    2. Game UI is primarily made up of 6x5 grid (6 guesses - 5 letters)
    3. WordleController contains a WordleModel instance, a guessState boolean (guess has been made)
        and a string buffer for capturing current input
    4. WordleModel holds list of Guess objects (guessesMade); accessible from this controller (getGuesses)
        - Guess objects includes: 
            - guess string
            - string list of letter evaluations [CORRECT, PRESENT, ABSENT] - determines color of grid cell
    - Game Loop:
        - key pressed (passed on as string to onKeyPress: single key, ENTER, or BACKSPACE)
            - refresh the screen
                - gameScore and guessCount
                - onscreen buffer (in current grid row, add/substract letters being typed)
                - screen guesses (when guess is made, guessState=True, add recent Guess to screen in correct colors)
                    - next buffer input should move to next row on grid
                - check isWon/isLost
    
    Example Layout:
    ----------------------------------------
        Game Score: 0    Guess Count: 1
        +-----+-----+-----+-----+-----+
        |  S  |  N  |  A  |  K  |  E  |
        +-----+-----+-----+-----+-----+
        |     |     |     |     |     |
        +-----+-----+-----+-----+-----+
        |     |     |     |     |     |
        +-----+-----+-----+-----+-----+
        |     |     |     |     |     |
        +-----+-----+-----+-----+-----+
        |     |     |     |     |     |
        +-----+-----+-----+-----+-----+
        |     |     |     |     |     |
        +-----+-----+-----+-----+-----+
        
        + onscreen keyboard maybe
    ----------------------------------------
    
    
'''



'''
WordleController Class
    - controller which interacts with UI
    - passes guesses to model, refreshes game
    - processes keys pressed in buffer
'''

class WordleController:
    def __init__(self):
        self.__model = WordleModel.WordleModel()
        self.__guessState = False
        self.__buffer = ""

        #local word bank for verification (not generation)
        valid_txt_path = os.path.join(os.path.dirname(__file__), "valid.txt")
        with open(valid_txt_path) as f:
            self.__valid_words = {i.strip().lower() for i in f}

    #when guess is made, pass to model
    def onGuess(self, guess:str):
        if not isinstance(guess, str):
            raise TypeError("Guess must be a string")
        if len(guess)==5:
            self.__model.makeGuess(guess)

    #whenever key is pressed, process (key should be passed as string from UI)
    def onKeyPress(self, key:str):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if len(self.__buffer)<=5:
            if key == "ENTER" and len(self.__buffer)==5 and self.isValid(self.__buffer): #valid guess entered
                self.onGuess(self.__buffer)
                self.__guessState = True
                self.__buffer = ""
            elif key=="BACKSPACE" and len(self.__buffer)>0: #backspace pressed - decrement guess buffer
                self.__buffer=self.__buffer[:-1]
            elif len(key)==1 and key.isalpha() and len(self.__buffer)<5: #key pressed - add to guess buffer
                self.__buffer=self.__buffer+key.lower()

    def refreshGame(self):
        if self.__model.isWon():
            self.__model.incrementGameScore()

    #getters/setters
    def getBuffer(self)->str:
        return self.__buffer
    def getGuessState(self)->bool:
        return self.__guessState
    def resetGuessState(self):
        self.__guessState = False

    #MODEL ROUTERS - win,loss,getters
    def isWon(self)->bool:
        return self.__model.isWon()
    def isLost(self)->bool:
        return self.__model.isLost()
    def getGameScore(self)->int:
        return self.__model.getGameScore()
    def getGuessCount(self)->int:
        return self.__model.getGuessCount()
    def getGuesses(self)->list:
        return self.__model.getGuesses()
    def getSecretWord(self)->str:
        return self.__model.getSecretWord()

    #UTIL
    def isValid(self, word:str)->bool: #validates guess as english word
        if word in self.__valid_words:
            return True
        else:
            #fallback api call (slow) for unique words
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            try:
                response = requests.get(url, timeout=5)
                if response.status_code==200: #definition returned (valid word)
                    return True
                else:
                    return False
            except requests.exceptions.Timeout:
                return False
