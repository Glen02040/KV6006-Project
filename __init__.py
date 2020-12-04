
import requests
from GUI_2 import prod_loc

store_loc = 'Newcastle UK'

# API key
api_file = open("google-api-key.txt", "r")
api_key = api_file.read()
api_file.close()

# home address input
store_addr = store_loc

# work address input
producer_addr = prod_loc

# base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get response
call = url + "origins=" + store_addr + "&destinations=" + producer_addr + "&key=" + api_key
print(call)
r = requests.get(call)

# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]

seconds = r.json()['rows'][0]['elements'][0]['duration']['value']

# print the total travel time
print("\nThe total travel time from home to work is", time)
