#! /usr/bin/python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

amazon_login = "https://www.amazon.com/gp/sign-in.html"
url = "https://www.amazon.com/giveaways"
options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=options)
winning_url = []

def main():
    # Login to Amazon
    browser.get(amazon_login)
    while(True):
        try:
            # Waits till the page is loaded (this is because the site is coded in react)
            wait = WebDriverWait(browser, 5).until(EC.title_is("Your Account"))
            break
        except Exception as e:
            print("Sign into your Amazon account.")

    browser.get(url)
    browser.find_element_by_id('a-autoid-0-announce').click()

    while(True):
        try:
            # Waits till the page loads (this is because the site is coded in react)
            wait = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'listing-info-container')))
            break
        except Exception as e:
            pass

    # Looks for the sepreate giveaways
    items = browser.find_element_by_class_name("listing-info-container").find_elements_by_tag_name('li')

    for item in items:
        requirement = item.find_element_by_class_name('a-text-bold').text
        print(requirement)

        if requirement == "No entry requirement":
            No_ent(item)
        elif requirement == "Watch a short video":
            video_ent(item)
            # browser.find_element_by_name("continue").click()

    #     try:
    #         is_win_text = soup.find("span", {'id': "title"})        # If you already didn't win, skips to next item
    #         print("already didn't win")
    #         print(is_win_text)
    #         if(is_win_text.split(", ")[1] == "you didn't win"):
    #             continue
    #     except Exception as e:
    #         pass
    #
    #     # wait = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'title')))
    #     time.sleep(2)
    #     is_win_text = browser.find_element_by_class_name("a-section a-spacing-none prize-header-container")
    #     print(is_win_text)
    #     if(is_win_text.split(", ")[1] == "you didn't win"):
    #         continue
    #     else:
    #         winning_url.append(browser.current_url)
    #
    # # print(browser.get_window_rect())
    # print(winning_url)

def No_ent(item):
    item.click()
    # try:
    #     browser.find_element_by_id("box_click_target").click()
    # except NoSuchElementException as e:
    #     pass

def video_ent(item):
    item.click()
    # try:
    #     browser.find_element_by_class_name("ytp-large-play-button ytp-button").click()
    #     time.sleep(15)
    # except NoSuchElementException as e:
    #     try:
    #         browser.find_element_by_id("airy-container").click()
    #         time.sleep(15)
    #     except NoSuchElementException as e:
    #         pass


main()
