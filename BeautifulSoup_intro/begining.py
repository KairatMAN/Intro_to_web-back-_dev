import requests
from bs4 import BeautifulSoup

url = 'https://lalafo.kg/kyrgyzstan/kompyutery/noutbuki-i-netbuki'
r = requests.get(url).text

data = BeautifulSoup(r, 'html.parser')

with open('data.html', 'a', encoding='utf-8') as f:
    f.write(str(data))
print("".join(data).prettify())



