import requests
import json
import matplotlib.pyplot as plt

url="https://www.okex.com"
data=requests.get(url+"/api/swap/v3/instruments/ticker").text
data=json.loads(data)
x=[]
y=[]
for d in data:
    x.append(d["instrument_id"])

for index,i in enumerate(x):
    d=requests.get(url+"/api/swap/v3/instruments/"+i+"/funding_time").text
    d=json.loads(d)
    y.append(float(d["funding_rate"]))
    i=str(i).replace("-USDT-SWAP","").replace("-USD-SWAP","")
    x[index]=i
    print(i+":"+d["funding_rate"])


# x=["BAND","CRV","BTC"]
# y=[-0.00014718,-0.00009366,-0.0003]
plt.figure(figsize=(25,4))
y, x = (list(t) for t in zip(*sorted(zip(y, x))))
plt.bar(x,y)
plt.show()
