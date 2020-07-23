import requests
from bs4 import BeautifulSoup
import time

def print_course(url):
    parser = 'lxml'
    if url == 'https://yandex.ru/':
        req = requests.get(url)
        soup = BeautifulSoup(req.text, parser)
        usd = soup.find('div', class_='inline-stocks__item_id_2002') #.find('span', class_='inline-stocks__value_inner')
        eur = usd.find_next_sibling()
        usd = usd.find('span', class_='inline-stocks__value_inner')
        eur = eur.find('span', class_='inline-stocks__value_inner')
        timee = soup.find('span', class_='inline-stocks__item__baloon_inner')
        time_text = time.strftime('%d-%m-%Y')
        eur_val = eur.text
        usd_val = usd.text
    elif url == 'https://cbr.ru/':
        req = requests.get(url)
        soup = BeautifulSoup(req.text, parser)
        usd = soup.find('div', class_='indicator_el indicator_course')
        eur = usd.find_next_sibling()
        timee = soup.find('div', class_='indicator_col-title')
        time_h = timee.text.strip().split('.')[-3]
        time_min = timee.text.strip().split('.')[-2]
        time_text = time.strftime('%d-%m-%Y')
        usd_val = usd.contents[-2].contents[-4].text.strip()
        eur_val = eur.contents[-2].contents[-4].text.strip()
    elif url == 'https://www.rambler.ru/':
        req = requests.get(url)
        soup = BeautifulSoup(req.text, parser)
        eur_sim = '€'
        usd = soup.find('div', class_='myKA')
        time_text = time.strftime('%d-%m-%Y')
        usd = usd.text.split(eur_sim)
        usd_val = usd[0][1:]
        eur_val = usd[-1]

    print(f'From {url} {time_text}:\nEuro: {eur_val}\nDollar: {usd_val}')

def main():
    url_yan = "https://yandex.ru/"
    url_cbr = 'https://cbr.ru/'
    url_rambler = 'https://www.rambler.ru/'
    url_arr = [url_yan, url_cbr, url_rambler]
    
    for i in url_arr:
        print_course(i)


if __name__ == "__main__":
    main()
    