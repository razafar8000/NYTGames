import json
import os

#A class thaat opens a word dictionary in json format 
class WordDictionary:

   
    def __init__(this, filename):
        this.__wordList = this.getWordList(filename)

    
    
    def getWordList(this, filename):
        # Resolve path relative to this file's location
        if not os.path.isabs(filename):
            filename = os.path.join(os.path.dirname(__file__), filename.replace('WordRepository/', ''))
        with open(filename, "r") as f:
            data = json.load(f)        
        wordList = set(data.keys())
        return wordList
 
    #checks to see if word exists in json file

    def contains(this, word):
        if(word in this.__wordList):
            return True    
        else:
            return False
        

    
