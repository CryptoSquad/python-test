import polpy
import numpy as np
from time import time
import time as t
import matplotlib.pyplot as plt
import sys

f = open('output.txt', 'w')
sys.stdout = f
start = time() - 12*2592000
end = time() - 6*2592000
c = polpy.Crypto('BTC_ETH',start,300,end)
t.sleep(1) # wait so not to overload the API
a= c.update()
c.timeArray()
q = c.avgArray()
fast =c.calcEMA(5)
slow = c.calcEMA(10)



w = c.plot(q,fast,slow)
c.backtest(fast,slow)

f.close()
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 1000)
# f = np.arange(0, 1000)
# #g = np.sin(np.arange(0, 10, 0.01) * 2) * 1000

# plt.plot(x, f, '-')
# #plt.plot(x, g, '-')

# #idx = np.argwhere(np.diff(np.sign(f - g)) != 0).reshape(-1) + 0
# #plt.plot(x[idx], f[idx], 'ro')
# plt.show()


'''
def backtest(avg,fast,slow):

	eth = 10
	z = []
	e = 0
	print(type(z))
	holding = True
	for i,j in enumerate(q):

		if 	fast[i] > 0 and round(fast[i],4) == round(slow[i],4):
			if fast[i-2] > slow[i-2] and holding:
				btc = eth * avg[i]
				eth = 0
				print('SELL')
				print('btc value ', btc)
				print('eth value ', eth)
				holding = False
				z.append(i)
			elif not holding:
				eth = btc / avg[i]
				btc = 0
				print('BUY')
				print('btc value ', btc)
				print('eth value ',eth)
				profit = (eth/10 - 1) * 100
				print('profit = ' + str(profit) + '% ')
				holding = True 
				z.append(i)
	return z


test = backtest(q,fast,slow)

x = range(0,len(q))
plt.plot(x, q, 'g')
plt.plot(x, fast)
plt.plot(x, slow)

for intersection in test:
	plt.plot(x[intersection], fast[intersection], 'ro')
plt.xlabel('Time')

plt.show()
'''