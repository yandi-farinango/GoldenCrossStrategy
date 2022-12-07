"""
Golden Cross Strategy 
"""

import math
import backtrader as bt 

# GoldenCross class extends bt.Strategy
class GoldenCross(bt.Strategy):
    # Order Percentage = % of cash we are investing 
    # Default ticker = SPY 
    params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95), ('ticker', 'SPY'))

    def __init__(self):
        # initialize indicators 
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, self.params.fast, plotname='50 Day Moving Average '
        )

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, self.params.slow, plotname='200 Day Moving Average '
        )

        # Cross over indicator takes in fast_moving_average, slow_moving_average 
        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)
    
    def next(self):
        pass

