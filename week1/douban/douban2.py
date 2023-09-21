import requests
from lxml import etree

import time


def get_from_url(urls):

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31'
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(url=urls, headers=header)

    one_page_info = etree.HTML(response.text)
    name_info = one_page_info.xpath('//div[@class="hd"]/a/span[1]/text()')
    for name in name_info:
        print(name)


def main():
    urls = tuple(
        f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))
    for url in urls:
        get_from_url(url)
        print('----')
        time.sleep(5)


if __name__ == "__main__":
    main()
