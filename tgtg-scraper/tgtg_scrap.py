import sys
import winsound
import time
from tgtg import TgtgClient


"""
run using sys
$ py tgtg_scrap.py john.smith@outlook.com
"""


email = sys.argv[1]
client = TgtgClient(email=email)
credentials = client.get_credentials()
access_token = credentials["access_token"]
refresh_token = credentials["refresh_token"]
user_id = credentials["user_id"]
client = TgtgClient(access_token=access_token, refresh_token=refresh_token, user_id=user_id)


def play_sound() -> None:
	duration = 700  # milliseconds
	freq = 440  # Hz
	winsound.Beep(freq, duration)


def main() -> None:
    while True:
        items = client.get_items()
        found = {elem["display_name"]: elem["items_available"] for elem in items if elem["items_available"] != 0}
        if found:
            play_sound()
            for name, amount in found.items():
                print(f"{name} - amount: {amount}")
        else:
            print("Nothing")
        time.sleep(10)


if __name__ == "__main__":
    main()
