"""
Script accepts command line arguments 

will run whatever strategy class we pass 
"""

import os, sys, argparse
import pandas as pd 
import backtrader as bt 
from backtrader import Cerebro
from strategies.GoldenCross import GoldenCross
from strategies.BuyHold import BuyHold

strategies = {
    'golden_cross': GoldenCross,
    'buy_hold': BuyHold, 
}

# Arguement parser to take strategies from command line 
parser = argparse.ArgumentParser()
parser.add_argument('strategy', help='Which Strategy to run', type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print('Invalid strategy, must be one of {}'.format(strategies.keys()))
    sys.exit()


cerebro = Cerebro()
cerebro.broker.setcash(100000)

spy_prices = pd.read_csv('data/spy.csv', index_col='Date', parse_dates=True)

# Feed data to Cerebro 
feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)

# Add strategy 
cerebro.addstrategy(strategies[args.strategy])

cerebro.run
cerebro.plot()







