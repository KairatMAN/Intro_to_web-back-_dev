import requests

# знанчения статус кода:
# 200 - ОК
# 301, 302 - перемещение на другой ресурс
# 404 - не найдено
# 500, 503, 504 - ошибка сервера

def google_search():
    url = 'http://www.google.com/search'

    for_sear = input('Что ищем? ')
    params = {'q': for_sear}

    response = requests.get(url, params=params)

    return print("text: ", response.text,
          "content: ", response.content,
          "status_code: ", response.status_code,
          "url: ", response.url,
          "hearders: ", response.headers,
          "encoding: ", response.encoding,
          "cookies: ", response.cookies,
          "history: ", response.history,
          "elapsed: ", response.elapsed,
          "request: ", response.request, sep="\n\n")


def weather_api():
    API_TOKEN = "6aabc5df3b437c7e6449947412809d20"
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'











