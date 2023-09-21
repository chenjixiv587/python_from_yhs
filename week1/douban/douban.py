from bs4 import BeautifulSoup as bs
import requests
import time


def get_from_url(urls):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(urls, headers=header)
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class', 'hd'}):
        for a_tag in tags.find_all('a',):
            for span_tag in a_tag.find_all('span', attrs={'class': 'title'}):
                print(f'the title is {span_tag.text}')


def main():
    pages = tuple(
        f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))
    for page in pages:
        get_from_url(page)
        print('-------')
        time.sleep(5)


if __name__ == "__main__":
    main()
