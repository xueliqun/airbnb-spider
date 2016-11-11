import time
from pages_parsing import room_info

while True:
    print(room_info.find().count())
    time.sleep(5)