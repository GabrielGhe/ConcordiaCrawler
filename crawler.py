import requests
from bs4 import BeautifulSoup

def crawl():
    url = "http://aits.encs.concordia.ca/oldsite/resources/schedules/courses/?y=2014&s=2"
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text)

    # get all the links
    for link in soup.findAll('a'):
        link_href = link.get('href')
        if link_href.startswith('details'):
            print( "{} {}".format(link.text, link_href) )

crawl()