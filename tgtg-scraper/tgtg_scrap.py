import sys
import winsound
import time
from datetime import datetime
from tgtg import TgtgClient
from geopy.geocoders import Nominatim


"""
run using sys
$ py tgtg_scrap.py john.smith@example.com Warszawa 30
mail, town, distance
"""


email = sys.argv[1]
location = sys.argv[2]
distance = int(sys.argv[3])
client = TgtgClient(email=email)
credentials = client.get_credentials()
access_token = credentials["access_token"]
refresh_token = credentials["refresh_token"]
user_id = credentials["user_id"]
client = TgtgClient(access_token=access_token,
                    refresh_token=refresh_token,
                    user_id=user_id)
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode(location)


def play_sound() -> None:
	duration = 700  # milliseconds
	freq = 440  # Hz
	winsound.Beep(freq, duration)


def main() -> None:
    while True:
        items = client.get_items(
            latitude=getLoc.latitude,
            longitude=getLoc.longitude,
            page_size=100)
        found = {elem["display_name"]: elem["items_available"] for elem in items if elem["items_available"] != 0 and elem["distance"] < distance}
        cur_time = datetime.now().strftime("%H:%M:%S")
        if found:
            play_sound()
            for name, amount in found.items():
                print(f"{cur_time} - {name} - amount: {amount}")
        else:
            print(f"{cur_time} - Nothing")
        time.sleep(10)


if __name__ == "__main__":
    main()
