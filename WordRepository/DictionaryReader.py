import pandas as pd
#A class thaat opens a word dictionary in json format 
class WordDictionary:

   
    def __init__(this, filename):
        this.__wordDataFrame = pd.read_csv(filename, typ='series')
        #puts key in order to force words as column 0 instead
        this.__wordDataFrame = pd.DataFrame(this.__wordDataFrame.keys())
    

    #gets a list of words that have a string length of n
    def getWordsOfLength(this, n):
        filteredDataFrame = this.__wordDataFrame[this.__wordDataFrame[0].str.len() == n]
        wordList = list(filteredDataFrame[0])
        return wordList

    

    
