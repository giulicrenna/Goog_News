import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url = 'https://news.google.com/news/rss'
client = urlopen(url)
xml_pag = client.read()
client.close

soup_page = soup(xml_pag, 'xml')
news_l = soup_page.findall('item')

for news in news_l:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("-"*60)