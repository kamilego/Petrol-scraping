import sys
import time
from calendar import monthrange
from datetime import datetime, timedelta

from dateutil import relativedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

days_dict = {
    "Monday": "Pon",
    "Tuesday": "Wt",
    "Wednesday": "Śr",
    "Thursday": "Czw",
    "Friday": "Pt",
    "Saturday": "Sob",
    "Sunday": "N"
}

months_dict = {
    "1": "Styczeń",
    "2": "Luty",
    "3": "Marzec",
    "4": "Kwiecień",
    "5": "Maj",
    "6": "Czerwiec",
    "7": "Lipiec",
    "8": "Sierpień",
    "9": "Wrzesień",
    "10": "Pażdziernik",
    "11": "Listopad",
    "12": "Grudzień"
}

PATH = r"C:\Users\kamil.legowicz\Downloads\chromedriver.exe"
WEBSITE = "https://www.google.pl/"
search_text = sys.argv[1] #"poznan majorka loty" 
ile = int(sys.argv[2])
splited_search_text = search_text.split()
rev_search_text = splited_search_text[::-1]
return_search_text = " ".join(rev_search_text)

service = Service(PATH)
options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(WEBSITE)

cookies = driver.find_element(By.ID, "L2AGLb").click()


def main(flights_seek: str, information: str) -> None:
    search = driver.find_element(By.ID, "APjFqb")
    search.send_keys(flights_seek)
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME, "oFoqE")[1].click()
    time.sleep(1)
    one = driver.find_elements(By.XPATH, "//div[@jsname='ibnC6b']")
    for elem in one:
        if "W jedną stronę" in elem.text:
            elem.click()

    day = datetime.today().day + 1
    month = datetime.today().month
    timestamp = f"{day}. {month}"

    timestamp_input = driver.find_element(By.CLASS_NAME, "oRRgMc").clear()
    timestamp_input = driver.find_element(By.CLASS_NAME, "oRRgMc")
    timestamp_input.send_keys(timestamp)
    timestamp_input.send_keys(Keys.ENTER)

    driver.find_element(By.CLASS_NAME, "eE8hUfzg9Na__overlay").click()

    time.sleep(1)

    month_sum = 3
    timestamp = datetime.today()
    nextmonth1 = timestamp + relativedelta.relativedelta(months=1)
    nextmonth2 = timestamp + relativedelta.relativedelta(months=2)
    for elem in [timestamp, nextmonth1, nextmonth2]:
        month_sum += monthrange(elem.year, elem.day)[1]

    data = {}

    for _ in range(month_sum):
        timestamp += timedelta(days=1)
        flights_list = driver.find_elements(By.CLASS_NAME, "ikUyY")
        for num, elem in enumerate(flights_list):
            # flight_connect = driver.find_element(By.CLASS_NAME, "u85UCd").text
            flight_connect = elem.text
            if "Bez przesiadek" in flight_connect:
                flight_time = driver.find_elements(By.CLASS_NAME, "sRcB8")[num].text
                airline = driver.find_elements(By.CLASS_NAME, "ps0VMc")[num].text
                price = driver.find_elements(By.CLASS_NAME, "GARawf")[num].text.replace("zł", "").replace(" ","")
                pol_day = days_dict[timestamp.strftime("%A")]
                pol_month = months_dict[str(timestamp.month)]
                if pol_month not in data:
                    data[pol_month] = {f"{timestamp.day:<2} {pol_day:<3}": [int(price), "Bez przesiadek", flight_time, airline]}
                else:
                    data[pol_month][f"{timestamp.day:<2} {pol_day:<3}"] = [int(price), "Bez przesiadek", flight_time, airline]
                break
            else:
                continue
        if _ != month_sum-1:
            driver.find_element(By.CLASS_NAME, "hLDSxb").click()
            time.sleep(0.6)


    print(information)
    print("-"*100)
    for key in data:
        data[key] = sorted(data[key].items(), key=lambda x: x[1])[:ile]
        data[key][0][1].append("Najtaniej")
        data[key] = sorted(data[key], key=lambda x: int(x[0].split()[0]))
        for k, v in data[key]:
            v = [str(elem) for elem in v]
            time_flight = v[2].split()
            hour = "".join(time_flight[:2])
            minutes = "".join(time_flight[-2:])
            v[2] = f"{hour} {minutes}"
            # print(f"{key:<11} {k} {v[0]} PLN | {hour} {minutes} | {v[3]} | {v[-1]}")
            print(f"{key:<11} {k} PLN", " | ".join(v))
        print("-"*100)

    search = driver.find_element(By.ID, "APjFqb").clear()

    return None

print("-"*100)
main(search_text, "PRZYLOT")
main(return_search_text, "ODLOT")

driver.quit()
