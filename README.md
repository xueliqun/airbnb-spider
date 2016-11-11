# airbnb-spider
Crawl room infomation from airbnb, including Place/Price/Title/Guests.    
I want to get all the New York room data in Airbnb.

1. get_room_urls.py gets all the link of every room from homepage, make a room_urls_list
2. pages_paring.py try to crawl room details from every_room_url, and store the data into MongoDB
3. main.py is used to import urls_list from get_room_urls.py and run the page_parse function of pages_parsing.py
4. When run main.py, run counts.py at the same time to count the number of room info we have gotten
5. After the data crawling, data_processing.py links to MongoDB to make data clean.
