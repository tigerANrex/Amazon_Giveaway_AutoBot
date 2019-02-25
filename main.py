#! /usr/bin/python

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

amazon_url = "https://www.amazon.com"
amazon_login = "https://www.amazon.com/gp/sign-in.html"
url = "https://www.amazon.com/giveaways"
browser = webdriver.Chrome()
# browser.get(amazon_login)                                                       # Login to Amazon
# while(True):
#     try:
#         wait = WebDriverWait(browser, 5).until(EC.title_is("Your Account"))
#         break
#     except Exception as e:
#         pass

browser.get(url)
soup = BeautifulSoup(browser.page_source, 'html.parser')

giveaway_href = soup.findAll("a", {"class": "a-button-text bxc-button-text"})[0].get('href')
giveaway_link = "".join((amazon_url, giveaway_href))

soup.decompose()
browser.get(giveaway_link) # Goes to givwaway page
while(True):
    try: # Waits till the page is loaded (this is because the site is coded in react)
        wait = WebDriverWait(browser, 1).until(EC.title_is("Amazon Giveaways"))
        break
    except Exception as e:
        pass
soup = BeautifulSoup(browser.page_source, "html.parser")

items = soup.findAll("a", {"class": "a-link-normal item-link"}) # Looks for the sepreate giveaways
print(len(items))
for i in items:
    requirement = str(i.find('span',{"class": "a-text-bold"}))[26:-7]
    print(requirement)
    if requirement == "No entry requirement":
        item_link = "".join((amazon_url, i.get('href')))
        print("No video: " + item_link)
    elif requirement == "Watch a short video":
        item_link = "".join((amazon_url, i.get('href')))
        print("video: " + item_link)
