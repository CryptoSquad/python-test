# using python poloniex wrapper
# install with : pip install https://github.com/s4w3d0ff/python-poloniex/archive/v0.3.6.zip 

import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import talib
from poloniex import Poloniex
from time import time
import time as t
import sys 


conn = sqlite3.connect('example.db')
c = conn.cursor()
#public
polo = Poloniex()

# private 
#polo = poloniex.Poloniex('your-Api-Key-Here-xxxx','yourSecretKeyHere123456789')



class Crypto(object):

	def __init__(self, currencyPair,  startDate=False, interval=False, endDate = False):

		self.currencyPair = currencyPair
		if interval not in [300, 900, 1800, 7200, 14400, 86400]:
			self.interval = 86400 # day 
		else:
			self.interval = interval
		if not startDate:
			startDate = time() - 2592000 # month
		if not endDate:
			self.lastDate = time() 
		else:
			self.lastDate = endDate
		self.data = polo.returnChartData(self.currencyPair, self.interval, startDate, self.lastDate) #returnChartData(self, pair, period=False, start=False, end=False)


	def update(self):
		# currentDate = time()
		# self.data.extend(polo.returnChartData(self.currencyPair, self.interval, self.lastDate, currentDate))
		# self.lastDate = currentDate

		return self.data

	def avgArray(self):
		self.avg = []
		for x in range(0,len(self.data)):
			self.avg.append(float(self.data[x]['weightedAverage']))
		self.avg = np.asarray(self.avg)
		return self.avg

	def timeArray(self):
		self.date = []
		for x in range(0,len(self.data)):
			self.date.append(float(self.data[x]['date']))


	def calcEMA(self,interval):
		out = talib.EMA(self.avg,interval)
		self.EMA= out
		return self.EMA

	def calcMACD(self,fastPeriod,slowPeriod):


		macd, signal, hist = talib.MACD(self.avg,fastperiod, slowperiod, signalperiod)
		
		self.MACD = macd - signal
		#print(self.MACD)
		#return self.macd

	def plot(self,data,algo1, algo2):#*args,algo2):
		
		
		x = range(0,len(self.data))
		plt.plot(x, data, 'g')
		plt.plot(x, algo1)
		plt.plot(x, algo2)
		# for y in args:
		# 	plt.plot(x,y)
		self.idx = np.argwhere(np.diff(np.sign( algo1 - algo2)) != 0).reshape(-1) + 0
		for intersection in self.idx:
			plt.plot(x[intersection], algo2[intersection], 'ro')
		plt.xlabel('Time')
		plt.ylabel(self.currencyPair)
		print 'Done'
		plt.show()

	def backtest(self,algo1,algo2):
		eth = 10
		holding = True
		trades = 0
		x = range(0,len(self.data))
		for i,j in enumerate(self.idx):
			# print(j)
			# print(algo1[j])

			if algo1[j-2] > algo2[j-2] and holding: # check that faster algo is above slower
				#buy
				btc = eth * self.avg[j]
				print('SELL')
				date = t.ctime(self.date[j])
				print(str(eth) + ' eth sold at ' + str(round(self.avg[j],5)))
				print(date)
				holding = False
				trades = trades + 1
				eth = 0
				print('btc value- %f' % btc)
				print('eth value- %f' % eth)
				print('\n')
			elif not holding:
				eth = btc / self.avg[j]
				print('BUY')
				profit = (eth/10 - 1) * 100
				date = t.ctime(self.date[j])
				print(str(eth) + ' eth bought at ' + str(round(self.avg[j],5)))
				print(date)
				print('profit = ' + str(profit) + '% ')
				holding = True
				trades = trades + 1 
				btc = 0
				print('btc value- %f' % btc)
				print('eth value- %f' % eth) 
				print('\n')
		print 'total trades = %i' % trades


