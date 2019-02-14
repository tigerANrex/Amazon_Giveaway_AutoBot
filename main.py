from bs4 import BeautifulSoup
from selenium import webdriver
import requests

amazon_url = "https://www.amazon.com"
url = "https://www.amazon.com/giveaways"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

giveaway_href = soup.findAll("a", {"class": "a-button-text bxc-button-text"})[0].get('href')
giveaway_link = "".join((amazon_url, giveaway_href))
r.close()
soup.decompose()

# r = requests.get(giveaway_link)
# print(r.text)
browser = webdriver.Chrome()
browser.get(giveaway_link)
soup = BeautifulSoup(browser.page_source, "html.parser")
items = soup.findAll("li", {"class": "a-section a-spacing-base listing-item"})
print(len(items))
