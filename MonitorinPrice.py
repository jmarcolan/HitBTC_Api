# Example of use of HitBtc API Class to monitoring price stock
# Developed by jmarcolan in Python 3.5.4 64 bit
# https://github.com/jmarcolan/HitBTC_Api
# if you like
# donate ETH: 0xb641e28C20574E968EB18dadd5060c33083a6b45
# donate BTC: 17tzJPnyJMsW2TRSi4TCTQ4YSawB6JkZU7



import requests
import json
import time
import sys
import winsound
import datetime
import tkinter


from HitBtc import public_api, trade_api
api_key    = "apiKey"
api_secret = "apiSecret"
nonce      = 1
hit = public_api()
# respost = hit.time()

# hitTra = trade_api(api_key,api_secret)
#print(respost)


def main():
    Freq = 100               # Set Frequency To 100 Hertz
    Dur = 800                # Set Duration To 800 ms == 0.8 second
    #future
    # window = tkinter.Tk()
    moneyCompra= 303                # 208.1
    moneyVenda = 322.21
    eth = 0.1563
    balance = 50.55




    while(True):

        #os.system('cls')
        tick = hit.ticker("ETHUSD")
        #tickLtc = hit.ticker("LTCUSD")

        print("The last value of Ether is  ", tick['last'])
        if(float(tick['last']) < 310):
            winsound.Beep(Freq*25,Dur)
        if(float(tick['last']) > 370):
            winsound.Beep(Freq, Dur)
            winsound.Beep(Freq*2 ,Dur)

        print('The spread are ', (float(tick['ask']) - float(tick['bid'])))
        print("In sell you will gain ",(float(tick['last'])-moneyCompra)*eth*0.997)


        #forma para ver quando vou ganhar na compra
        print("In buy you will gain ", (moneyVenda-float(tick['last']))*(balance/float(tick['last'])*0.998))
        print("In buy you will gain in ETH " , (balance/float(tick['last']) - eth)*0.998)

        time.sleep(5)



if __name__ == "__main__":
    #tick = hit.ticker("ETHUSD")
    #print(datetime.datetime.fromtimestamp(int(tick['timestamp'])).strftime('%Y-%m-%d %H:%M:%S'))


    main()
