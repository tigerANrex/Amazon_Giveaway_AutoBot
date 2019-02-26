#! /usr/bin/python

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

amazon_url = "https://www.amazon.com"
amazon_login = "https://www.amazon.com/gp/sign-in.html"
url = "https://www.amazon.com/giveaways"
browser = webdriver.Chrome()
winning_url = []

def main():
    browser.get(amazon_login)                                                       # Login to Amazon
    while(True): # Waits till the page is loaded (this is because the site is coded in react)
        try:
            wait = WebDriverWait(browser, 5).until(EC.title_is("Your Account"))
            break
        except Exception as e:
            pass

    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    giveaway_href = soup.findAll("a", {"class": "a-button-text bxc-button-text"})[0].get('href')
    giveaway_link = "".join((amazon_url, giveaway_href))

    soup.decompose()
    browser.get(giveaway_link) # Goes to givwaway page
    while(True):
        try: # Waits till the page loads (this is because the site is coded in react)
            wait = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'listing-info-container'))) #.title_is("Amazon Giveaways"))
            break
        except Exception as e:
            pass
    soup = BeautifulSoup(browser.page_source, "html.parser")

    items = soup.findAll("a", {"class": "a-link-normal item-link"}) # Looks for the sepreate giveaways
    for i in items:
        requirement = str(i.find('span',{"class": "a-text-bold"}))[26:-7]
        if requirement == "No entry requirement":
            item_link = "".join((amazon_url, i.get('href')))
            No_ent(item_link)
        elif requirement == "Watch a short video":
            item_link = "".join((amazon_url, i.get('href')))
            video_ent(item_link)
            browser.find_element_by_name("continue").click()

        try:
            is_win_text = soup.find("span", {'id': "title"})        # If you already didn't win, skips to next item
            print("already didn't win")
            print(is_win_text)
            if(is_win_text.split(", ")[1] == "you didn't win"):
                continue
        except Exception as e:
            pass

        # wait = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'title')))
        time.sleep(2)
        is_win_text = browser.find_element_by_class_name("a-section a-spacing-none prize-header-container")
        print(is_win_text)
        if(is_win_text.split(", ")[1] == "you didn't win"):
            continue
        else:
            winning_url.append(browser.current_url)

    # print(browser.get_window_rect())
    print(winning_url)

def No_ent(url):
    browser.get(url)
    time.sleep(5)
    try:
        browser.find_element_by_id("box_click_target").click()
    except NoSuchElementException as e:
        pass

def video_ent(url):
    browser.get(url)
    time.sleep(5)
    try:
        browser.find_element_by_class_name("ytp-large-play-button ytp-button").click()
        time.sleep(15)
    except NoSuchElementException as e:
        try:
            browser.find_element_by_id("airy-container").click()
            time.sleep(15)
        except NoSuchElementException as e:
            pass


main()
