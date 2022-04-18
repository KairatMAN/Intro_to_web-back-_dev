import requests
# from bs4 import BeautifulSoup

url = 'https://lalafo.kg/kyrgyzstan/kompyutery/noutbuki-i-netbuki'

params = {'Date': 'Sun, 1 Apr 2022 08:10:01 GMT'}
response = requests.get(url, params=params)
# data = BeautifulSoup(response, 'html.parser')
#
# noutes = data.find_all('div')
#
#
# json_data = response.json(**kwargs)
# print(json_data)

print(response.text)
# print("\n\n\n\n",type(response.text))
# print(len(response.text))
#
# with open('lalafo.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)


