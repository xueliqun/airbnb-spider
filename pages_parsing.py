import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost',27017)
airbnb = client['airbnb']
room_info = airbnb['room_info']
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'cookie':'p3_mt=treatment; p1_searchbar=control; p1_new_eligible=31; sdid=; ftv=1478622422476; mdr_browser=desktop; nuxSrvy=true; _csrf_token=V4%24.airbnb.com%24J5zHi2Y95Zk%24FIb-AZzqJD48EVEr04dPje3O-A6RcpZc39cIM27PnFY%3D; _airbed_session_id=77a5916005013f9a3567a41b866c7f35; flags=268435456; bev=1478622420_IALVl45UVDigJj3f; _user_attributes=%7B%22curr%22%3A%22USD%22%2C%22guest_exchange%22%3A1.0%2C%22device_profiling_session_id%22%3A%221478626773--4f16c90cef50f890b064ccea%22%2C%22giftcard_profiling_session_id%22%3A%221478626773--72ba8c43179ed4ccde9a2320%22%7D; EPISODES=s=1478627449425&r=https%3A%2F%2Fwww.airbnb.com%2Frooms%2F15092550'
}
#url = 'https://www.airbnb.com/rooms/15727768'

def get_room_info(url):

    web_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.select('span#listing_name > div > span')[0].text
    place = '-'.join([i.strip() for i in soup.select('a.link-reset > span > span')[0].text.split(',')[:2]])
    price = int(soup.select('span#book-it-price-string > span.h3 > span')[0].text.split('$')[1])
    guests = int(soup.select('div > div.col-sm-4.hide-md.hide-lg > span')[1].text.split(' ')[0])
    #room_info.insert_one({'Title':title, 'Price':price, 'Place':place, 'Guests_num':guests})
    #print({'Title':title, 'Price':price, 'Place':place, 'Guests_num':guests})
#get_room_info(url)
