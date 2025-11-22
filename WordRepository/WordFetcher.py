import requests

url = "https://random-word-api.vercel.app/api?words=1&length=5"


#fetches random word of length n from api
def fetchWord(n) -> str:
    try:
        url = "https://random-word-api.vercel.app/api?words=1&length=" + str(n) 
        response = requests.get(url, timeout=5)
        wordString = response.json()[0]
        return wordString
    except requests.exceptions.Timeout:
        print("ERROR: Request timed out")
        return None


#---------------------------------
#testing
def test_fetch():
    newWord = fetchWord()
    if newWord is not None:
        print(newWord)
    else:
        print("ERROR: No word found")

# test_fetch()