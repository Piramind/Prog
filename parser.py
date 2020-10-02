import requests
from bs4 import BeautifulSoup

URL = https://auto.ru/cars/ford/mondeo/all/

HEADERS = ("")

def get_html(url, params=None):
    r = request.get(url, headers=HEADERS, params=params)
    return  r

def grt_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("a", class_='na-card-item')

    cars = []
    for item in items:
        cars.append(('title': item.find('div', class_='na-card-name').get_text()))
    print(cars)


def parse():
    HTML = get_html(URL)
    if html.status_code == 200:
        pass
    else:
        print("Error")

parse()