from datetime import datetime
import MetaTrader5 as mt5
from datetime import datetime, timedelta
import statistics
import time
import numpy as np
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# import pytz module for working with time zone
import pytz
 
# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime.strptime("01.01.2018", "%d.%m.%Y") # datetime(2020, 1, 10, tzinfo=timezone)
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, utc_from, 10080)

print('Start Measurement')
stt = time.perf_counter()

rerates = np.zeros((len(rates), 8), dtype=float)
for i in range(len(rates)):
    for x in range(8):
        rerates[i][x] = rates[i][x]

cd = {}
cd["EURUSD"] = rerates
open_s = ["EURUSD"]
means_data = {}
period = 8
ohlc = 4 # open high low close 0.time 1.open 2.high 3.low 4.close 5.tick_volume 6.spread 7.real_volume


# print(type(rerates))
# print(type(rerates[0]))
# print(rerates.shape)
# print(rerates.max(axis=0))
# print(rerates)
# print(rates)
"""
for f in open_s:
    means_data[f] = [0, 0, 0, 0]
    means_data[f][0] = statistics.mean([i[ohlc] for i in cd[f]]) # ANSmean 

    period_number = int(timedelta(hours=period).seconds/60)
    
    fset = [] # set of all peakdiffs for f
    for i in range(len(cd[f])):
        period_candle_set = cd[f][i:i+period_number] # every candle that is after i-th candle and is less than period of time
        peakvalue = period_candle_set.max(axis=0)[ohlc]
        peakdiff = peakvalue - cd[f][i][ohlc] 
        if peakdiff > 0:
            fset.append(peakdiff)
    
    s_1 = len(fset) / len(cd[f])

    means_data[f][1] = statistics.mean(fset)
    means_data[f][2] = statistics.stdev(fset)
    means_data[f][3] = s_1


print(f'Means: {means_data}')
print(f'Time: {time.perf_counter() - stt}')
"""

"""st = utc_from
while True:
    f = "EURUSD"
    st += timedelta(minutes=1)
    rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, st, 1)
    if rates[0][0] != cd[f][-1][0]:
        cd[f] = np.roll(cd[f], -1)
        for x in range(8):
            cd[f][-1][x] = rates[0][x]
        print(cd[f][-1])
"""