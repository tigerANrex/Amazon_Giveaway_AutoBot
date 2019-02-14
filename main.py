from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/giveaways"
r = requests.get(url).text

print(r)
# soup = BeautifulSoup(r)
