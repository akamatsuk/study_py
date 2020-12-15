from bs4 import BeautifulSoup
import requests

file = open("expocity.txt", "w")
base_url = "https://mitsui-shopping-park.com/lalaport/expocity/shopguide/?start="
num = 0
while num <= 500:
    url=base_url+ str(num)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    titles =soup.find_all("dt", class_="shop-name")
    num += 40
    for title in titles:
        file.write(title.text + "\n")
file.close()