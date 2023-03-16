#Copyright (c) 2023, Austin Fisher
#All rights reserved.
#
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

import requests
from bs4 import BeautifulSoup


# Getting page, id appears to increase by 1 per race  750 skipped?
URL = "https://www.espn.com/f1/results/_/id/600026747"
page = requests.get(URL)

 
# Parsing the HTML
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='fittPageContainer')

qualiTable = results.find('table', class_='RacingSessions__Table')

pole = qualiTable.find('tbody').find_all('tr')[3].find_all('td')[1].find('div', class_='GamestripRacing__Athlete__Name truncate').text

print(qualiTable.find('tbody').find_all('tr')[3].find_all('td')[1].find('div', class_='GamestripRacing__Athlete__Name truncate').text + ' Pole')

table = results.find('table', class_='Table')

#print(racer.prettify())

for racers in table.find_all('tbody'):
    rows = racers.find_all('tr')
    #print(rows)

for row in rows:
    name = row.find_all('td')[1].find('span', class_='dn show-mobile TeamLinks__abbrev').text
    position = row.find_all('td')[0].text

    #point calc
    if position == '1':
        points = 25
    elif position == '2':
        points = 18
    elif position == '3':
        points = 15
    elif position == '4':
        points = 12
    elif position == '5':
        points = 10
    elif position == '6':
        points = 8
    elif position == '7':
        points = 6
    elif position == '8':
        points = 4
    elif position == '9':
        points = 2
    elif position == '10':
        points = 1
    else:
        points = 0

    if(name == pole):
        points += 1;


    if (row.find_all('td')[6].text == '--'):
        fastest = ''
    else:
        if(int(position) < 11):
            points += 1
        fastest = ' fastest lap'

    print(name + ' ' + position + ' ' + str(points) + fastest)

#first = racer.find('span', class_='dn show-mobile TeamLinks__abbrev')

#print(first.text)

