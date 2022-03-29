from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'

data = requests.get(url).text

html_data = BeautifulSoup(data,'html.parser')

quotes = html_data.find_all(class_='quote')
schet = 0
for quote in quotes:
    result = quote.find(class_='text')
    author = quote.find(class_="author")
    schet +=1
    print(schet,")",sep="")
    print(result.get_text(),author.get_text(),sep="\tby  ",end="\n")
# print(html_data.get_text())