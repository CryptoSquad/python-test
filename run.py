import polpy
import numpy as np
import pandas as pd
from time import time
import time as t
import matplotlib.pyplot as plt
import sys


start = time() - 5*1800
end = time() - 3*1800
c = polpy.Crypto('BTC_ETH',start,300,end)
 # wait so not to overload the API
c.update()
# c.timeArray()
# q = c.avgArray()
# fast =c.calcEMA(10)
# slow = c.calcEMA(20)



# df.drop(df.tail(1).index)
#c.data.plot(x = 'date', y = 'weightedAverage', style = 'o')

c.data.weightedAverage = c.data.weightedAverage.astype('float64')


for a in range(0,len(c.data.date),1):
	c.data.date.iloc[a] = t.ctime(c.data.date.iloc[a])

print c.data.date
# c.data.plot(x = 'date', y = 'weightedAverage', style = 'o')

# plt.show()