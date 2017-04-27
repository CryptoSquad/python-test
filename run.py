import polpy

pair = raw_input('Enter Currency Pair (ex BTC_ETH):  ')
polpy.dbInit(pair)
polpy.dbInsert(pair)
polpy.calcEMA(pair)
