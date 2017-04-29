# using python poloniex wrapper
# install with : pip install https://github.com/s4w3d0ff/python-poloniex/archive/v0.3.6.zip 

import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import talib
from poloniex import Poloniex
from time import time

conn = sqlite3.connect('example.db')
c = conn.cursor()
#public
polo = Poloniex()

# private 
#polo = poloniex.Poloniex('your-Api-Key-Here-xxxx','yourSecretKeyHere123456789')


class Crypto(object):

	def __init__(self, currencyPair, currrentPrice, startDate=False, interval=False, endDate = False):

		self.currencyPair = currencyPair
		self.currrentPrice = 0
		if interval not in [300, 900, 1800, 7200, 14400, 86400]:
            self.interval = 86400 # day 
        else:
        	self.interval = interval
        if not startDate:
            start = time() - 2592000 # month
        if not end:
            end = time() 
        self.lastDate = end
		

	def dbInit(self):
		
		sql = 'CREATE TABLE IF NOT EXISTS ' + self.currencyPair + ' (volume real, quoteVolume real, high real, low real, date text, close real, weightedAverage real, open real)'
		c.execute(sql)

	def dbInsert(self):
		
		temp = polo.returnChartData(self.currencyPair, self,interval, self.startDate, self.lastDate) #returnChartData(self, pair, period=False, start=False, end=False)
		for data in temp:
			sql = 'INSERT INTO ' + self.currencyPair + ' VALUES (?,?,?,?,?,?,?,?)'
			#convert from unicode to float
			c.execute(sql, [data['volume'], data['quoteVolume'], data['high'], data['date'], data['low'], data['close'], data['weightedAverage'], data['open']])
			
		conn.commit()	
		#conn.close()

	def dbDrop(self):
		sql = 'DROP TABLE ' + self.currencyPair
		c.execute(sql)

	def calcEMA(self):
		sql = 'SELECT weightedAverage FROM ' + currencyPair
		c.execute(sql)
		data = c.fetchall() # data is returned as a tuple
		for x in range(0,len(data)):
			data[x] = data[x][0]
		#print(data)
		dataNP = np.asarray(data) # cast as numpy array 
		out = talib.EMA(dataNP,500)

	def 
	def plot(self,data):
		########## INCOMPLETE
		plt.plot(x, data, 'g', x, out, 'r')
		plt.xlabel('Time')
		plt.ylabel('BTC/ETH price')
		plt.show()