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

    #dosent work yet
    def tradesTimeStamp(self,tpair,beginPeriod,endPeriod):
        request = self.url + "/api/1/public/" + tpair+"/trades?"
        request = request + "from="+beginPeriod+"&till="+endPeriod     #"from=0&by=trade_id&sort=desc&start_index=0&max_results=100"
        request = request + "&by=trade_id" + "&format_timestamp=second"
        response = requests.get( request)
        print(response.content)
        return json.loads(response.content)
        
    
        
class trade_api:
    def __init__(self, name):
        self.key = name




