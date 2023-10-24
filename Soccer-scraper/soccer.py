from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sys

"""
py soccer.py 5 2.4
"""

last_matches = int(sys.argv[1])
avg_goals = float(sys.argv[2])
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

# go forward _th days 
for _ in range(2):
    next_day = driver.find_element(By.CLASS_NAME, "calendar__navigation--tomorrow").click()
    time.sleep(1)

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

print()
print(f"Analyzing last -{last_matches}- matches where AVG goals are greater than -{avg_goals}-")
print()
for league, matches in events_dict.items():
    print(league)
    print("-"*30)
    for match in matches:
        time.sleep(1)
        match.click()
        time.sleep(1)
        new_window = driver.window_handles
        driver.switch_to.window(new_window[1])
        tabs = driver.find_elements(By.CLASS_NAME, "tab__tab")
        for num, tab in enumerate(tabs):
            tab_text = tab.get_attribute('innerHTML')
            if 'H2H' in tab_text:
                tab.click()
        time.sleep(2)
        groups = driver.find_elements(By.CLASS_NAME, "h2h__section")
        group_dict = {}
        for group in groups:
            team_title = group.find_element(By.CLASS_NAME, "section__title").text
            results = group.find_elements(By.CLASS_NAME, "h2h__result")[:last_matches]   
            goal_sum = 0
            for match in results:
                goals = [int(elem) for elem in match.text.split("\n")]
                goal_sum += sum(goals)
            group_dict[team_title] = round(goal_sum/last_matches, 2)
        # print(group_dict)
        if all([result >= avg_goals for result in list(group_dict.values())[:2]]):
            for key, value in group_dict.items():
                print(f"{key:<35}", value)
            print("-"*5)
        driver.close()
        driver.switch_to.window(new_window[0])
driver.close()