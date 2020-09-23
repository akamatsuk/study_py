import requests
from bs4 import BeautifulSoup

res = requests.get('http://quotes.toscrape.com/')

soup = BeautifulSoup(res.text, 'html.parser')

title_text = soup.find('title').get_text()
print(title_text)
# >> Quotes to Scrape
