# using python poloniex wrapper
# install with : pip install https://github.com/s4w3d0ff/python-poloniex/archive/v0.3.6.zip 

import sqlite3
import numpy as np
import pandas as pd
import talib
from poloniex import Poloniex
import matplotlib.pyplot as plt

conn = sqlite3.connect('example.db')
c = conn.cursor()
#public
polo = Poloniex()

# private 
#polo = poloniex.Poloniex('your-Api-Key-Here-xxxx','yourSecretKeyHere123456789')

def dbInit(currencyPair):
	
	sql = 'CREATE TABLE IF NOT EXISTS ' + currencyPair + ' (volume real, quoteVolume real, high real, low real, date text, close real, weightedAverage real, open real)'
	c.execute(sql)

def dbInsert(currencyPair):
	
	temp = polo.returnChartData(currencyPair) #returnChartData(self, pair, period=False, start=False, end=False)
	for data in temp:
		sql = 'INSERT INTO ' +currencyPair + ' VALUES (?,?,?,?,?,?,?,?)'
		#convert from unicode to float
		c.execute(sql, [data['volume'], data['quoteVolume'], data['high'], data['date'], data['low'], data['close'], data['weightedAverage'], data['open']])
		
	conn.commit()	
	#conn.close()

def calcEMA(currencyPair):
	
	sql = 'SELECT weightedAverage FROM ' + currencyPair
	c.execute(sql)
	data = c.fetchall() # data is returned as a tuple
	for x in range(0,len(data)):
		data[x] = data[x][0]
	#print(data)
	dataNP = np.asarray(data) # cast as numpy array 
	out = talib.EMA(dataNP,15)
	print(np.shape(dataNP))
	x = list(range(0,len(data)))
	# plt.plot(list(x, data,'r',x , out, 'g')
	# plt.show()
	plt.plot(x, data, 'g', x, out, 'r')
	plt.xlabel('30 day window')
	plt.ylabel('BTC/ETH price')
	plt.show()


	#print(type(data[1]))
	#floatData = [float(x) for x in data] #talib no likey non float variables 	
	#out = talib.SMA(floatData,15)



