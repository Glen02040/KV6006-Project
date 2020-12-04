"""
Created on Wed Dec  2 16:00:12 2020

@author: Ki
"""

import requests
#import smtplib

# API key
api_file = open("google-api-key.txt", "r")
api_key = api_file.read()
api_file.close()

# home address input
home = input("Enter a home address\n")

# work address input
work = input("Enter a work address\n")

# base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get response
call = url + "origins=" + home + "&destinations=" + work + "&key=" + api_key
print(call)
r = requests.get(call)

# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]

seconds = r.json()['rows'][0]['elements'][0]['duration']['value']

# print the total travel time
print("\nThe total travel time from home to work is", time)