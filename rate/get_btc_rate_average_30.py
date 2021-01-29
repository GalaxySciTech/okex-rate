import json
from decimal import Decimal

import requests
import time

num = 0
sum = 0

for i in range(1, 14):
    url = "https://www.okexcn.com/v2/perpetual/pc/public/fundingRate?contract=BTC-USD-SWAP&current=" + str(
        i) + "&t=" + str(time.time())
    data = requests.get(url).text
    data = json.loads(data)
    list = data["data"]["fundingRates"]
    for y in list:
        num += 1
        # print(y["realFundingRate"])
        sum += Decimal(y["realFundingRate"])

rate = sum / num
ave_rate = rate * 3 * 100
print("okex永续合约日息:", ave_rate, "%")
print("okex永续合约月息", ave_rate * 30, "%")
print("okex永续合约年息", ave_rate * 30 * 12, "%")
