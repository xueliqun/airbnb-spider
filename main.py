from get_room_urls import room_urls
from pages_parsing import get_room_info

import time


for link in set(room_urls.split()):
    try:
        get_room_info(link)
    except(IndexError):
        pass