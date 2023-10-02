import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import smtplib
import ssl

email_from = "vinaayakgaikwad@gmail.com"
email_to = "vinaayakgaikwad@gmail.com"
url="https://codeforces.com/contests"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")


table = soup.find('table')
headers = table.find_all('th')

titles = []
for i in headers:
    titles.append(i.string)

del titles[4:]

contestDateTime = table.find_all('span',{'class':'format-time'})
contestTime = []
for i in contestDateTime:
    contestTime.append(i.text)

latestContests = []
i = 1
while(i<len(table.find_all('tr'))):
    latestContests.append(table.find_all('tr')[i].find('td').string)
    i+=1

codeForcesLatestContests = []
for i in latestContests:
    i = repr(i)
    codeForcesLatestContests.append(i)


url1 = "https://atcoder.jp/contests/"
r1 = requests.get(url1)
soup1 =BeautifulSoup(r1.text,"lxml")
atCoderTable = soup1.find('div',{'id':'contest-table-upcoming'})
atCoderTableContestsTime = atCoderTable.find_all('time')

for i in atCoderTableContestsTime:
    contestTime.append(i.text)

atCoderTableContestsName = atCoderTable.find('td').find_all('a')
atCoderNameList = atCoderTable.tbody.select('a:nth-of-type(odd)')

for i in atCoderNameList:
    codeForcesLatestContests.append(i.text)


url2 = "https://www.hackerearth.com/challenges/"
r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.text,"lxml")

hackEarthTable = soup2.find('div',{'class':'upcoming challenge-list'})
hackEarthContestTag = hackEarthTable.find_all('span',{'class':'challenge-list-title challenge-card-wrapper'})

for i in hackEarthContestTag:
    codeForcesLatestContests.append(i.text)

hackEarthDateTag = soup2.find_all('div',{'class':'date less-margin dark'})

for i in hackEarthDateTag:
    contestTime.append(i.text)

df = pd.DataFrame({"Name of Contests:":codeForcesLatestContests, "Date and Time of Contests:":contestTime})

df.to_excel("Contests.xlsx")
print('1) File generated successfully')
