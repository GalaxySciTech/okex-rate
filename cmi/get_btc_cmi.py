import requests
from datetime import datetime, timedelta
from decimal import *
import json

end = datetime.today()
end_time = end.strftime("%Y-%m-%dT00:00:00.000Z")
start = end - timedelta(days=30)
start_time = start.strftime("%Y-%m-%dT00:00:00.000Z")

url = "https://www.okex.me/api/spot/v3/instruments/BTC-USDT/candles?granularity=86400&start=" + start_time + "&end=" + end_time
data = requests.get(url).text
data=json.loads(data)
max_list_close = []
min_list_close = []
for d in data:
    max_list_close.append(Decimal(d[4]))
    min_list_close.append(Decimal(d[4]))

max = max(max_list_close)
min = min(min_list_close)


cmi=abs((Decimal(data[0][4])-Decimal(data[29][4]))/(max-min))*100
print("当前cmi值为:"+cmi)