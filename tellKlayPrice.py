import json
import urllib.request
from urllib.request import Request, urlopen

def get(cur): #cur = symbol of currency
    urlTicker = urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all')
    readTicker = urlTicker.read()
    jsonTicker = json.loads(readTicker)
    FindCur = jsonTicker[cur]['last']
    out = int(float(FindCur))
    return out
  

  
import telegram

with open("keys.txt","r") as f:
    for line in f.readlines():
        name_key = line.split(" : ")
        if name_key[0]="telegram":
            token = name_key[1]
            break

bot = telegram.Bot(token)
updates = bot.getUpdates()
#print(updates[0].message.chat_id)

def sendTel(text):
    bot.sendMessage(chat_id=1733943603, text=text)
    


from time import sleep

while True:
    price = get('klay')
    sendTel(f'KLAY 시세는 {price}원 입니다')
    sleep(600)