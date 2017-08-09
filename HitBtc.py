#HitBtc API Class
#Developed by jmarcolan in Python 3
#https://github.com/jmarcolan/HitBTC_Api
#if you like
#donate ETH: 0xb641e28C20574E968EB18dadd5060c33083a6b45

'''
API Documentation:
 * Public API v1 (https://hitbtc.com/api#marketrestful)
'''

import json, requests


class public_api(object):
    def __init__(self):
        self.url= 'http://api.hitbtc.com'

    def time(self):
        response = requests.get( self.url + "/api/1/public/time")
        print(response.content)
        return json.loads(response.content)
    
    def symbols(self):
        response = requests.get( self.url +"/api/1/public/symbols")
        print(response.content)
        return json.loads(response.content)

    def ticker(self,tpair):
        # example hit.ticker("ETHUSD")
        response = requests.get( self.url +"/api/1/public/"+tpair+"/ticker")
        print(response.content)
        return json.loads(response.content)
    
    def orderbook(self, tpair):
        response = requests.get( self.url +"/api/1/public/"+tpair+"/orderbook")
        print(response.content)
        return json.loads(response.content)
    
    def trades(self, tpair):
        response = requests.get( self.url +"/api/1/public/"+tpair+"/trades")
        print(response.content)
        return json.loads(response.content)
        
    
        
class trade_api:
    def __init__(self, name):
        self.key = name



hit= public_api()
respost = hit.time()

print(respost)
#print(respost['timestamp'])
