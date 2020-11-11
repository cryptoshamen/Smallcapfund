import pandas as pd
import requests

url = 'https://dex.binance.org/api/v1/ticker/24hr'
APItic = pd.DataFrame(requests.get(url).json())

a = APItic['symbol']
n = 0
#upphere we are obtaining symbols for all available exchange options (theyre 153)

while n < 153:
       n = n + 1
       
       symb = a[n]
       #downhere you can change time interval: (change 1d for: 1m, 5m, 15m 1h, 4h,1w, 1m and so on)
       inter = "&interval=1d"
       url2 = f"https://dex.binance.org/api/v1/klines?symbol=" \
       f"{symb}" \
       f"{inter}"   
       Data = pd.DataFrame(requests.get(url2).json())
       print(Data)
       
       #downhere we gonna save our obtained data to excel files
       
       sym = a[n]
       typ = ".xlsx"
       
       #downhere you need to type your path dir instead of D:\ (wprowadź folder w ktorym umiesciles folder Pikny)
       path = f"D:\Pikny\Data\Data" \
       f"{sym}" \
       f"{typ}"    
       print(Data.to_excel(path))
       
       #downhere we gonna save our obtained data to csv files
       sym = a[n]
       typ = ".csv"
       path = f"D:\Pikny\Data\Data" \
       f"{sym}" \
       f"{typ}" 
       print(Data.to_csv(path))
       