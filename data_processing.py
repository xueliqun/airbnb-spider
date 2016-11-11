from pages_parsing import room_info
import pymongo
client = pymongo.MongoClient('localhost',27017)
airbnb = client['airbnb']
room_infoX = airbnb['room_infoX']
for i in room_infoX.find():
    room_infoX.update({'_id':i['_id']}, {'$set' : {'Cost_per_guest': round(i['Price']/float(i['Guests_num']),2)}})
    #room_infoX.update({'_id':i['_id']}, {'$push': {'Cost_per_guest':round(float(i['Price'])/i['Guests_num'])}})
    print(i)