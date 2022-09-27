import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
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
res=""
if bool(re.search(r"\s", inpt)):
    inpt_1=inpt.split()

    for x in range(0, len(inpt_1)-1):
        res=res + inpt_1[x]+ "%20"

    res=res+ inpt_1[len(inpt_1)-1]
else:
    res=inpt
num_news=int(input("Enter number of news you want: "))
news_link = f"https://news.google.com/rss/search?q={res}&hl=en-IN&gl=IN&ceid=IN:en"
news(news_link, num_news)