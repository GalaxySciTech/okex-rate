import json
from decimal import Decimal

import requests
import time

num = 0
sum = 0

for i in range(1, 5):
    url = "https://www.okex.me/v2/perpetual/pc/public/fundingRate?contract=BTC-USD-SWAP&current=" + str(
        i) + "&t=" + str(time.time())
    data = requests.get(url).text
    data = json.loads(data)
    list = data["data"]["fundingRates"]
    for y in list:
        num +=1
        # print(y["realFundingRate"])
        sum += Decimal(y["realFundingRate"])

rate = sum / num
print("okex永续合约30日平均费率:", rate *3)
