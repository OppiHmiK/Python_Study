# -*- coding : utf-8 -*-

from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req
import pandas as pd
import sys, os

response = req.get('http://watch.peoplepower21.org/Euian')
html = response.text
soup = bs(html, 'lxml')

body = soup.body
ea_list = body.find(id = 'ea_list')
table = ea_list.table
tbody = table.tbody

bill_list = []
lines = tbody.find_all('tr')
for line in lines:
    td_list = line.find_all('td')

    bill_list.append(
        [ td_list[0].text, td_list[1].text, td_list[2].text, td_list[4].text ])

thead = table.thead
th_list = thead.find_all('th')

df = pd.DataFrame(bill_list, columns = [th_list[0].text,
                                        th_list[1].text,
                                        th_list[2].text,
                                        th_list[4].text] )

df.to_csv('bill.csv')