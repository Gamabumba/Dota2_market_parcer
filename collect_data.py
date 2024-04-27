import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from operations_with_file import create_file, write_in_file
from time import sleep


def collect_data():
    url = "https://market.dota2.net"
    ua = UserAgent()

    headers = {
        'user-agent': ua.random,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cookie': '_csrf=I2BrNvAQeauU8dNTqvgS92JxbRKfod5X; goon=0; _ga=GA1.2.1217819274.1677907168; _ym_uid=16155676843106663; _ym_d=1677907168; d2mid=8fbjal2V1zbuFkIUZckSFekpPpaEwT; _gid=GA1.2.1352333945.1678379074; _ym_isad=1; PHPSESSID=591adc120123291ed882ff6c2986abf6; _ym_visorc=w; d2netAuthStatus=checked'
    }

    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')

    total_pages = soup.find(id="total_pages").text

    create_file()

    for curr_page in range(int(total_pages)-1):
        url = f"https://market.dota2.net/?p={curr_page+1}&sd=desc"
        req = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')

        items = soup.find(id="applications").find_all(class_="item")
        if items:
            for item in items:
                link = 'https://market.dota2.net'+item.get("href")

                inner_req = requests.get(url=link, headers=headers)
                inner_soup = BeautifulSoup(inner_req.text, 'lxml')

                try:
                    item_name = inner_soup.find(class_="item-h1").find(style="color: #000000").text
                except:
                    item_name = 'None'

                try:
                    hero_name = inner_soup.find(class_="item-h1").find(class_="item-appearance").text
                except:
                    hero_name = 'None'

                try:
                    item_type = inner_soup.find(class_="item-tags").text
                except:
                    item_type = 'None'

                try:
                    curr_price = inner_soup.find(class_="ip-bestprice").text
                except:
                    curr_price = 'None'

                try:
                    min_price = inner_soup.find(class_="rectanglestats").find_all(class_="rectanglestat")[1].find('b').text
                except:
                    min_price = 'None'

                try:
                    max_price = inner_soup.find(class_="rectanglestats").find_all(class_="rectanglestat")[3].find('b').text
                except:
                    max_price = 'None'

                try:
                    avg_price = inner_soup.find(class_="rectanglestats").find_all(class_="rectanglestat")[2].find('b').text
                except:
                    avg_price = 'None'

                try:
                    buys_call = inner_soup.find(class_="rectanglestats").find_all(class_="rectanglestat")[0].find('b').text
                except:
                    buys_call = 'None'

                write_in_file(link, item_name, hero_name, item_type, curr_price, min_price, max_price, avg_price, buys_call)

                sleep(1)

            sleep(4)

        print(f'пройдена {curr_page+1} страница')
