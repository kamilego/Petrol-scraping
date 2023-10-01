from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

website_url = r"https://www.flashscore.com/"

chromedriver_path = r"C:\Users\default.DESKTOP-E4TLVMN\Downloads\chromedriver.exe"
service = Service(chromedriver_path)
options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get(website_url)
time.sleep(2)
cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
button = driver.find_element(By.CLASS_NAME, "wizard__closeButton").click()

events = driver.find_elements(By.CSS_SELECTOR, '.soccer')[1]
events_text = events.get_attribute('innerHTML')
events_text = events_text.replace('<div class="event__header', '<div id="event__header')
events_list = events_text.split("</div><div id=")
for num, elem in enumerate(events_list):
    if '"event__header"' in elem:
        number = num
        break

events = driver.find_elements(By.CSS_SELECTOR, '.pinned, .event__match')[:number]
events_dict = {}
for num, elem in enumerate(events):
    elem_text = elem.get_attribute('innerHTML')
    if "wizard__relativeWrapper" in elem_text:
        title = elem.find_element(By.CLASS_NAME, "event__title--name")
        soccer_league = title.text
        events_dict[soccer_league] = []
    else:
        events_dict[soccer_league].append(elem)

for key, value in events_dict.items():
    print(key)
    for v in value:
        print(v.text)