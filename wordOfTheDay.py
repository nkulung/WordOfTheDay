import requests
from bs4 import BeautifulSoup as bs
import urllib3




s = requests.get('http://dictionary.reference.com/wordoftheday/').text
soup = bs(s, "html.parser")
wordDay = soup.find("div", {"class": "definition-header"})
wordRaw = wordDay.text
wordList = []
wordRaw = wordRaw.split()

print('The Word of the Day is:',wordRaw[2])

input('Press ENTER to exit')




                  
