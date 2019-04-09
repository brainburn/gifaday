import os
from twilio.rest import Client
import requests
import schedule
import time

TWILIO_ACCT_SID = os.getenv('TWILIO_ACCT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

SOURCE_NUM = os.getenv('SOURCE_NUM')
TARGET_NUM = os.getenv('TARGET_NUM')
DEBUG_NUM = os.getenv('DEBUG_NUM')

GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

def get_random_gif():
    req_str = "https://api.giphy.com/v1/gifs/random?api_key=%s&tag=funny dog&rating=G"%GIPHY_API_KEY
    r = requests.get(req_str)
    r.raise_for_status()
    link = r.json()['data']['url']
    return link

def send_text():
    twilio_client = Client(TWILIO_ACCT_SID, TWILIO_AUTH_TOKEN)
    link = get_random_gif()
    print(link)
    twilio_client.messages.create(body=link, from_=SOURCE_NUM,to=TARGET_NUM)

schedule.every().day.at("08:11").do(send_text)

while True:
    schedule.run_pending()
    time.sleep(3600)
