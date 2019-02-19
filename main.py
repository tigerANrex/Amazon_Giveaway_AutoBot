from bs4 import BeautifulSoup
from selenium import webdriver

amazon_url = "https://www.amazon.com"
url = "https://www.amazon.com/giveaways"
browser = webdriver.Chrome()
browser.get(url)
soup = BeautifulSoup(browser.page_source, 'html.parser')

giveaway_href = soup.findAll("a", {"class": "a-button-text bxc-button-text"})[0].get('href')
giveaway_link = "".join((amazon_url, giveaway_href))
soup.decompose()

browser.get(giveaway_link)
soup = BeautifulSoup(browser.page_source, "html.parser")
item_list = soup.findAll("a", {"class": "a-link-normal item-link"})
# print(item_list[0].get('href'))
for items in item_list:
    item_link = "".join((amazon_url, items.get('href')))
    print(item_link)                                          # Prints the URL for each items
    # browser.get(item_link)
    # soup2 = BeautifulSoup(browser.page_source, 'html.parser')

    # lose_text = soup.findAll("span", {"class": "a-size-base-plus a-color-secondary qa-giveaway-result-text a-text-bold"})[0]
    # print(lose_text)


###Avery's code

items = soup.findAll("li", {"class": "a-section a-spacing-base listing-item"})
for i in items:
    requirement = str(i.find('span',{"class": "a-text-bold"}))[26:-7]
    print(requirement)
    #if  is in requirement:
     #   href = i.get('href')
      #  print(href)
