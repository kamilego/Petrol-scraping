import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def scrap_site() -> list:
    link = r"https://moto.trojmiasto.pl/paliwa/"
    website = requests.get(link)
    soup = BeautifulSoup(website.text, "html.parser")
    table = soup.find(class_="prices-table")
    body = table.select("tr")[1:-2]
    return body


def save_scrapped_petrol_data(body: list, file_name_path: str) -> None:
    petrol_dict = {}
    for elem in body:
        price = elem.find("span", {"class": "prices-table__price"})
        date_state = elem.find("span", {"class": "prices-table__date"})
        if price != "Brak ceny" and date_state is not None:
            p_station_name = elem.find("h3", {"class": "prices-table__name"}).text.strip()
            p_station_location = elem.find("span", {"class": "prices-table__location"}).text.strip()
            date_state = date_state.text.strip()
            price = float(price.text.strip()[:4].replace(",", "."))
            if date_state == "dziś":
                petrol_dict[p_station_name, p_station_location] = price
    with open(file_name_path, "w", encoding="utf-8") as file_read:
        for key, value in petrol_dict.items():
            file_read.write(f"{key[0]}: {value}zł, {key[1]}\n")
    return petrol_dict


def load_petrol_data(folder_name: str) -> dict:
    data_list = os.listdir(folder_name)
    petrol_read_dict = {}
    for file in data_list:
        file_name_path = os.path.join(folder_name, file)
        with open(file_name_path, "r", encoding="utf-8") as file_read:
            petrol_data = file_read.readlines()
            date = file.replace(".txt", "")
            petrol_read_dict[date] = []
            for elem in petrol_data:
                if "Gdańsk" in elem and "Baltic" not in elem:
                    petrol_read_dict[date].append(elem.replace("\n", ""))
            petrol_read_dict[date] = petrol_read_dict[date][0]
    return petrol_read_dict


def plot_graph(data_dict: dict) -> None:
    for date, price in data_dict.items():
        data_dict[date] = float(price.split(",")[0].split()[-1][:-2])
    data_dict = {k: data_dict[k] for k in sorted(list(data_dict.keys()), key=lambda x: datetime.strptime(x, '%d-%m-%y'))}
    graph = plt.bar(x=data_dict.keys(), height=data_dict.values(), width=0.3)
    min_value = min(list(data_dict.values()))
    min_index = list(data_dict.values()).index(min_value)
    max_value = max(list(data_dict.values()))
    max_index = list(data_dict.values()).index(max_value)
    graph[max_index].set_color("r")
    graph[min_index].set_color("g")
    plt.title("Wykres najniższych cen paliw")
    plt.xlabel("Data")
    plt.ylabel("Cena za litr [zł]")
    plt.ylim([round(min_value-0.1, 1), round(max_value+0.1, 1)])
    plt.xticks(rotation=45)
    for num, data in enumerate(data_dict.values()):
        plt.text(num, data+0.01, str(data), ha="center")
    plt.show()


def execution_func(folder_name: str) -> None:
    todays_date = datetime.now().strftime("%d-%m-%y")
    file_check_path = os.path.join(folder_name, todays_date+".txt")
    if not os.path.exists(file_check_path):
        scrapped_element = scrap_site()
        save_scrapped_petrol_data(scrapped_element, file_check_path)
    petrol_read_dict = load_petrol_data(folder_name)
    plot_graph(petrol_read_dict)


def main():
    folder_name = "saved_data"
    execution_func(folder_name)


if __name__ == '__main__':
    main()
