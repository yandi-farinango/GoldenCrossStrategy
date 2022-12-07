"""
Script accepts command line arguments 

will run whatever strategy class we pass 
"""

import os, sys, argparse
import pandas as pd 
import backtrader as bt 
from backtrader import Cerebro
from strategies.GoldenCross import GoldenCross

cerebro = Cerebro()
cerebro.broker.setcash(100000)

spy_prices = pd.read_csv('data/spy.csv', index_col='Date', parse_dates=True)

# Feed data to Cerebro 
feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)

# Add strategy 
cerebro.addstrategy(GoldenCross)

cerebro.run
cerebro.plot()






