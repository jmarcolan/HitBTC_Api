from HitBtc import public_api, trade_api

# get api_key and api_secret on https://hitbtc.com/settings/api-keys
api_key    = "apiKey" 
api_secret = "apiSecret"
nonce      = 1



hit= public_api()
respost = hit.time()

hitTra = trade_api(api_key,api_secret)
print(respost)
#print(respost['timestamp'])

#hitTra.new_order("ETHUSD","buy","0.001",200)
