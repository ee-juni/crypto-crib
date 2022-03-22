# Volatility Break-out strategy
# 변동성 돌파 전략

import pyupbit
from time import sleep
import datetime

with open("keys.txt","r") as f:
    for line in f.readlines():
        name_key = line.split(" : ")
        if name_key[0]="upbit":
            access_key, secret_key = name_key[1].split(",") 
            break

upbit = pyupbit.Upbit(access_key, secret_key)



def get(cur):
    bal = upbit.get_balances()
    print(bal)
    ko = bal[0]['balance']
    do = ""
    for c in bal:
        if c['currency']==cur:
            do = c['balance']
            break
    ko = str(round(float(ko)*0.9995))
    if cur=="KRW": return ko
    else: return do

def getTarget(cur, interval):
    df = pyupbit.get_ohlcv("KRW-"+cur, interval=interval, count=2)
    df = df.values.tolist() #open high low close volume
    target = df[1][0]+(df[0][1]-df[0][2])/2
    return round(target)

def buy_crypto_currency(cur):
    ko = get("KRW")
    print(upbit.buy_market_order("KRW-"+cur, ko)) # KO 만큼 시장가 매수

def sell_crypto_currency(cur):
    do = get(cur)
    print(upbit.sell_market_order("KRW-"+cur, do))
    


cur = "BTC"
interval = "minute60"

target_price = getTarget(cur, interval)

while True:
    print("Target:", getTarget(cur, interval), end=", ")
    current_price = int(pyupbit.get_current_price("KRW-"+cur))
    print("Current:", current_price)
    
    now = str(datetime.datetime.now())
    time = now.split(" ")[1].split(":")
    second = int(float(time[2]))
    if (int(float(time[1]))==0) and (second==0 or second==1):
        target_price = getTarget(cur, interval)
        sell_crypto_currency(cur)
    if current_price > target_price:
        buy_crypto_currency(cur)
        
    sleep(0.4)
    
