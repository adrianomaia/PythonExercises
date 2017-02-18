'''
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage.
'''
# I'm using this website because is the one I use to se series :)

import requests
from bs4 import BeautifulSoup

url = "http://www.watchepisodeseries.com/"
r = requests.get(url)
storyList = []

soup = BeautifulSoup(r.text,"html5lib")
titles = soup.findAll('div',{'class': 'va'})

for row in titles:
    storyList.append(row.text)

print (storyList)
