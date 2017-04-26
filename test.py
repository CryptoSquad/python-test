# using python poloniex wrapper
# install with : pip install https://github.com/s4w3d0ff/python-poloniex/archive/v0.3.6.zip 

import sqlite3
import csv
from poloniex import Poloniex

conn = sqlite3.connect('example.db')
c = conn.cursor()
#public
polo = Poloniex()

# private 
#polo = poloniex.Poloniex('your-Api-Key-Here-xxxx','yourSecretKeyHere123456789')
#print(polo.marketTradeHist('BTC_ETH'))

c.execute('''CREATE TABLE btc_eth
             (volume real, quoteVolume real, high real, low real, date text, close real, weightedAverage real, open real)''')


a = polo.returnChartData('BTC_ETH') # def returnChartData(self, pair, period=False, start=False, end=False):x

for data in a:
	c.execute("INSERT INTO btc_eth VALUES (?,?,?,?,?,?,?,?)", [data['volume'], data['quoteVolume'], 
		data['high'], data['date'], data['low'], data['close'], data['weightedAverage'], data['open']])
	#print(data['volume'])
conn.commit()
for row in c.execute('SELECT * FROM btc_eth ORDER BY volume'):
	print row
conn.close()

#for x in a:
#	out.writerow(x)