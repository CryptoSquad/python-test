import polpy
import numpy as np
from time import time

start = time() - 2*2592000
end = time() - 2592000
c = polpy.Crypto('BTC_ETH',start,1800,end)
a= c.update()
q = c.avgArray()
fast =c.calcEMA(5)
slow = c.calcEMA(10)



w = c.plot(q,fast,slow)
c.backtest(fast,slow)

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