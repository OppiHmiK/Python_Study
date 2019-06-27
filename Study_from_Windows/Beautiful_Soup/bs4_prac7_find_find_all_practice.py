from bs4 import BeautifulSoup as bs
import requests as req

with open('html.txt', 'rb') as html:
    html = html.read()

soup = bs(html, 'lxml')

title_data = soup.find('h1')
print(title_data)
print(title_data.string)
print(title_data.get_text())
print('\n')

paragraph_data = soup.find('p')
print(paragraph_data)
print(paragraph_data.string)
print(paragraph_data.get_text())
print('\n')

title_data_2 = soup.find(id = 'title')
print(title_data_2)
print(title_data_2.string)
print(title_data_2.get_text())
print('\n')

paragraph_data_2 = soup.find('p', 'cssstyle')
print(paragraph_data_2)
print(paragraph_data_2.string)
print(paragraph_data_2.get_text())
print('\n')

paragraph_data_3 = soup.find('p', attrs = {'align' : 'center'})
print(paragraph_data_3)
print(paragraph_data_3.string)
print(paragraph_data_3.get_text())
print('\n')

paragraph_data_4 = soup.find_all('p')
print(paragraph_data_4)
print(paragraph_data_4[0].get_text())
print(paragraph_data_4[1].get_text())
print('\n')

