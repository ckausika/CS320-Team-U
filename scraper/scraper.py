#Python program to scrape website  
import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "https://www.cics.umass.edu/people/all-faculty-staff" 
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html.parser') 
   
profs=[]  # a list to store quotes 
links = []

i = 0
professors = soup.find_all('div', attrs = {'class': 'views-field views-field-title'})
for row in professors:
    a = row.find("a")
    profs.append(a.text)
    links.append(a['href'])
    print(a, "\n")
    i+= 1

print(profs)
print(links)
print(len(profs))
print(len(links))
print("total: ", i)