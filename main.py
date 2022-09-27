import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

def news(news_url,counter):
    context=ssl.create_default_context()
    client=urlopen(news_url,context=context)
    xml_page=client.read()
    client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")

    i=0

    for news in news_list:
        if i == counter:
            break
        print(f"news #{i + 1}: {news.title.text}")
        i = i+1


inpt = input("Enter the name of the company you want to search: ")
num_news=int(input("Enter number of news you want: "))
news_link = f"https://news.google.com/rss/search?q={inpt}&hl=en-IN&gl=IN&ceid=IN:en"
news(news_link, num_news)