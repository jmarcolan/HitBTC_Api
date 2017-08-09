from HitBtc import public_api, trade_api


api_key    = 'secret'
api_secret = 'secret'
nonce      = 1



hit= public_api()
respost = hit.time()

print(respost)
#print(respost['timestamp'])
