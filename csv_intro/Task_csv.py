import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2FshareArticle%3Furl%3Dchrome%3A%2F%2Fnewtab%2F%26title%3DNew%2520Tab'

response = requests.get(url).text

with open('linkedin.html', 'w') as f:
    f.write(response)

soup = BeautifulSoup(response, 'html.parser')
form = soup.find_all('div', class_='haAclf')
print(form.text)
