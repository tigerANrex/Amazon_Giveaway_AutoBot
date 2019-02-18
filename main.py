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
item_list = soup.findAll("a", {"class": "a-link-normal item-link"})
# print(item_list[0].get('href'))
for items in item_list:
    item_link = "".join((amazon_url, items.get('href')))
    r2 = requests.get(item_link)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    print(r2.url)
    # lose_text = soup.findAll("span", {"class": "a-size-base-plus a-color-secondary qa-giveaway-result-text a-text-bold"})[0]
    # print(lose_text)
