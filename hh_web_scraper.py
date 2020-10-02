# -*- coding: utf-8 -*-
 
import requests
from bs4 import BeautifulSoup
import time
 
# достает html код по указанной ссылке
 
 
def get_html(url, f=True):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    rq = requests.get(url, headers=headers)
    if(f):
        print('Getting HTML-code from ', url)
    return rq.text
 
 
# проверяет, есть ли на странице ссылки на вакансии
def is_empty(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('resume-serp_block-result-action')
    if links == []:
        return True
    else:
        return False
 
 
# функция, которая для данного запроса и региона ищет все страницы с результатами поиска и набирает большой список со всеми ссылками на вакансии
# возвращает список ссылок по запросу query в регионе с кодом area
def get_all_resumes_links(query, area):
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url_base = 'https://hh.ru/search/resume?clusters=True'
    url_area = '&area='+area
    url_base2 = '&order_by=relevance&logic=normal&pos=position&exp_period=all_time&no_magic=False&st=resumeSearch'
    url_text = '&text='+query
    url_page = '&page='
 
    # когда не найдем с помощью bs4 нужный элемент, то выставим его False
    # нужен для остановки цикла перебора всех страниц
    page_is_not_empty = True
 
    all_links = []
    page = 1
 
    for i in range(1):
        url = url_base + url_area+url_base2 + url_text + url_page + str(i)
        # time.sleep(.5)
        html = get_html(url)
        all_links = get_resumes_links(html, all_links)
        """if not is_empty(html):
            all_links = get_resumes_links(html, all_links)
 
            page += 1
        else:
            page_is_not_empty = False
        """
    return all_links
 
 
# функция, которая собирает все ссылки на вакансии на странице поиска
# принимает список, который уже может быть не пустой, возвращает дополненный список
def get_resumes_links(html, all_links):
    # новый объект класса BeutifulSoup
    soup = BeautifulSoup(html, 'lxml')
 
    links = soup.find_all('a', class_='resume-search-item__name')
    for link in links:
        link_parsed = ("http://hh.ru") + link.get('href')
        all_links.append(link_parsed)
    return all_links
 
 
def parse_exp_in_resume(soup):  # Функция, которая парсит блок с опытом работы
    # находим общий опыт работы
    all_exp = soup.find_all('div', class_='resume-block__experience-timeinterval')
    s = soup.find(
        'span', class_='resume-block__title-text resume-block__title-text_sub').get_text()
    if "Опыт работы" not in s:  # если человек вообще не работал
        return
    print(s)
    s = s.split()
    total_exp = 0  # Общий опыт работы в месяцах
    # Считам общий стаж
    if(len(s) == 6):
        total_exp = int(s[2])*12 + int(s[4])
    elif(s[3] == "год" or s[3] == "лет" or s[3] == "года"):
        total_exp = int(s[2])*12
    else:
        total_exp = int(s[2])
    print("Общий стаж: ", total_exp)
    cur_exp = 0
    s *= 0
    # Рассматриваем каждый опыт работы
    for exp in all_exp:
        print(exp.get_text())
        s = exp.get_text().split()
        if(len(s) == 4):
            cur_exp = float(s[0])*12 + float(s[2])
        elif(s[1] == "год" or s[1] == "лет" or s[1] == "года"):
            cur_exp = float(s[0])*12
        else:
            cur_exp = float(s[0])
        if(cur_exp/total_exp >= 0.5):
            print("ПОДХОДИТ!")
    print("=========")
 
 
    # функция, которая парсит блок с описанием вакансии и возвращает дополненный словарь, который ей дали на входе
"""    def parse_description_in_offer(soup, description_dict):
        # описание вакансии
        description = soup.find('div', class_='b-resume-desc-wrapper')
        # оставим только текст без тегов
        # text = ''.join(description.findAll(text=True))
        # почистим текст от знаков препинания
        for elem in ('.',',',';',':','"'):
            if elem in text:
                text = text.replace(elem, ' ')
 
        # проверим каждое слово и занесем его в словарь
        for word in text.split(' '):
            if word.lower() in description_dict:
                description_dict[word.lower()] += 1
            else:
                description_dict[word.lower()] = 1
 
        return description_dict
"""
"""
 
# функция, которая парсит основные регионы со страницы https://hh.ru/search/resume
# и сохраняет название региона и его код для GET запроса в файл
# функция нужна для себя - чтобы знать, какой код региона использовать
 def get_and_save_area_codes():
    html = get_html('https://hh.ru/search/resume?area=1347')
    # time.sleep(.3)
    soup = BeautifulSoup(html, 'lxml')
    # areas_parsed = []
 
    # нашли все объекты, которые содержат название региона и его код
    pairs = soup.find('div', class_='clusters-group').find_all('a', class_='clusters-value')
 
    # выделяем текст региона и кода, записываем в файл
    with open('area_codes02.txt', 'w', encoding='utf-8') as f:
        for pair in pairs:
            area = pair.find('span', class_='clusters-value__name').get_text()
            code = pair.get('href').split('&')[2].split('=')[1]
            f.write(area+' '+code+'\n')
 
    print('DONE')
"""
"""
def parse_resumes(links):
    skill_dict = {}
    description_dict = {}
    for link in links:
        html = get_html(link)
        # time.sleep(.3)
        soup = BeautifulSoup(html, 'lxml')
        skill_dict = parse_skills_in_resume(soup, skill_dict)
        description_dict = parse_description_in_offer(soup, description_dict)
 
    # запишем навыки в файл skills_freq
    skills_sorted = sorted(skill_dict.items(), key=lambda x: x[1], reverse = True)
    with open('skill_freq.txt', 'w', encoding='utf-8') as f:
        for skill in skills_sorted:
            f.write(skill[0]+' '+str(skill[1])+'\n')
 
    # запишем слова из описаний в файл descriptions_freq
        descriptions_sorted = sorted(description_dict.items(), key=lambda x: x[1], reverse = True)
    with open('description_freq.txt', 'w', encoding='utf-8') as f:
        for description in descriptions_sorted:
            f.write(description[0]+' '+str(description[1])+'\n')
"""
 
if __name__ == '__main__':
    query = 'менеджер+по+продажам'
    area = '2'
    # сначала вытащим все ссылки на резюме по данному запросу и региону
    links = get_all_resumes_links(query, area)
    # теперь распарсим информацию по каждой ссылке, полученной выше
    # parse_resumes(links)
    for link in links:
        html = get_html(link, False)
        # time.sleep(.3)
        soup = BeautifulSoup(html, 'lxml')
        parse_exp_in_resume(soup)
    print('Проверено', len(links), 'вакансий.')