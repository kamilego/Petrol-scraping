import sys
import time
from calendar import monthrange
from datetime import datetime, timedelta

from dateutil import relativedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
py sele.py "gdansk malaga loty" 5
"""

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


def get_driver() -> None:
    chromedriver_path = r"C:\Users\kamil.legowicz\Downloads\chromedriver.exe"
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    
    global driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return None


def load_website(direction: str, search_flights: str) -> None:
    search = search_flights.split()
    if direction == "PRZYLOT":
        search = search[::-1]
    search = "+".join(search)
    website_url = f"https://www.google.pl/search?q={search}"
    driver.get(website_url)
    return None


def format_flight_time(time_flight: str) -> str:
    split_time = time_flight.split()
    hour = "".join(split_time[:2])
    if len(split_time[3]) == 1:
        split_time[3] = f"0{split_time[3]}"
    minutes = "".join(split_time[-2:])
    return f"{hour} {minutes}"


def main(information: str, amount: int, today_date: datetime) -> list:
    time.sleep(1)
    if information == "ODLOT":
        cookies = driver.find_element(By.ID, "L2AGLb").click()
    driver.find_elements(By.CLASS_NAME, "oFoqE")[1].click()
    time.sleep(5)
    one = driver.find_elements(By.XPATH, "//div[@jsname='ibnC6b']")
    for elem in one:
        if "W jedną stronę" in elem.text:
            elem.click()

    day = today_date.day + 1
    month = today_date.month
    timestamp = f"{day}. {month}"

    timestamp_input = driver.find_element(By.CLASS_NAME, "oRRgMc").clear()
    timestamp_input = driver.find_element(By.CLASS_NAME, "oRRgMc")
    timestamp_input.send_keys(timestamp)
    timestamp_input.send_keys(Keys.ENTER)
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "eE8hUfzg9Na__overlay").click()

    time.sleep(1)

    month_sum = 3
    nextmonth1 = today_date + relativedelta.relativedelta(months=1)
    nextmonth2 = today_date + relativedelta.relativedelta(months=2)
    for elem in [today_date, nextmonth1, nextmonth2]:
        month_sum += monthrange(elem.year, elem.day)[1]

    data = {}
    month_sum = 30
    for _ in range(month_sum):
        today_date += timedelta(days=1)
        flights_list = driver.find_elements(By.CLASS_NAME, "ikUyY")
        for num, flight in enumerate(flights_list):
            flight_connect = flight.text
            if "Bez przesiadek" in flight_connect:
                flight_time = driver.find_elements(By.CLASS_NAME, "sRcB8")[num].text
                flight_time = format_flight_time(flight_time)
                airline = driver.find_elements(By.CLASS_NAME, "ps0VMc")[num].text
                price = driver.find_elements(By.CLASS_NAME, "GARawf")[num].text.replace("zł", "").replace(" ","")
                day_name = days_dict[today_date.strftime("%A")]
                month_name = months_dict[str(today_date.month)]
                if month_name not in data:
                    data[month_name] = {f"{today_date.day:<2} {day_name:<3}": [int(price), "Bez przesiadek", flight_time, f"{airline:<9}"]}
                else:
                    data[month_name][f"{today_date.day:<2} {day_name:<3}"] = [int(price), "Bez przesiadek", flight_time, f"{airline:<9}"]
                break
            else:
                continue

        if _ != month_sum-1:
            driver.find_element(By.CLASS_NAME, "hLDSxb").click()
            time.sleep(0.6)

    flights = [information, "-"*100]
    for month in data:
        data[month] = sorted(data[month].items(), key=lambda x: x[1])[:amount]
        data[month][0][1].append("Najtaniej")
        data[month] = sorted(data[month], key=lambda x: int(x[0].split()[0]))
        for day, description in data[month]:
            result = f"{month:<11} {day} | PLN {description[0]:<4} | " + " | ".join(description[1:])
            flights.append(result)
        flights.append("-"*100)

    return flights

def save_files(list_data: list, today_date: datetime) -> None:
    string_timestamp = today_date.strftime("%Y%m%d_%H%M%S")
    with open(f"flights/flight_{string_timestamp}.txt", "a") as f:
        for elem in list_data:
            f.write(f"{elem}\n")
            print(elem)
    return None

if __name__ == "__main__":
    search_text = sys.argv[1]
    amount = int(sys.argv[2])
    now = datetime.now()
    get_driver()
    for event in ["ODLOT", "PRZYLOT"]:
        load_website(event, search_text)
        f = main(event, amount, now)
        save_files(f, now)
    driver.quit()
