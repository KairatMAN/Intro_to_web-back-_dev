from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'



data = requests.get(url).text
html_data = BeautifulSoup(data,'html.parser')


quotes = html_data.find_all(class_='quote')
counter = 0

for quote in quotes:
    text = quote.find(class_='text')
    author = quote.find(class_="author")
    tags = quote.find(class_="keywords")
    counter +=1
    print(counter,")",sep="")
    print(text.get_text(),author.get_text(),sep="\tby  ",end="\n")
    print("Tags:",tags['content'])
# print(html_data.get_text())re