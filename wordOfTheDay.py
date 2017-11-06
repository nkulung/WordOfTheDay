import requests
from bs4 import BeautifulSoup as bs
import urllib3

def getWord():
    s = requests.get('http://dictionary.reference.com/wordoftheday/').text
    soup = bs(s, "html.parser")
    wordDay = soup.find("div", {"class": "definition-header"})
    wordRaw = wordDay.text
    wordList = []
    wordRaw = wordRaw.split()
    return wordRaw
def main():
    word = getWord()
    word = word[2]
    print('The Word of the Day is:',word)
    input('Press ENTER to Exit')

main()

    




                  
