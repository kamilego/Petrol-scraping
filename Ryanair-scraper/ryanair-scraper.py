import requests
from bs4 import BeautifulSoup
from selenium import webdriver


link = r"https://www.google.pl/"
link2 = r"https://www.kayak.pl/flights/GDN-PFO/2022-05-01/2022-05-05?sort=bestflight_a"
path = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(link)
# website = requests.get(link)
# soup = BeautifulSoup(website.text, "html.parser")
# b = soup.find("inner-grid keel-grid")

