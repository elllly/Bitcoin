import requests
from datetime import datetime
import pytz

def btc_function(a):
    BTC_Rate.append(data['bpi'][list_data[a]]['rate'])
    BTC_Rate[a] = int(float(BTC_Rate[a].replace(',', '')))
    return BTC_Rate[a]
    
    
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()

Time_Site = data['time']['updated']
tz_Req_GMT = pytz.timezone('Europe/London')
datetime_Req_GMT = datetime.now(tz_Req_GMT)
print('Requested Time:', datetime_Req_GMT.strftime('%H:%M:%S'))

list_data = ['USD', 'EUR', 'GBP']
Symbol = ['\u0024', '\u20ac', '\u00a3']
BTC_Rate = []

for i in range(0, 3):
    print('BTC in', list_data[i], 'at', Time_Site, 'is:', Symbol[i], btc_function(i))
