# Import the 'backtrader' library and alias it as 'bt'.
import backtrader as bt
import datetime

# Define a custom trading strategy class named 'RSIStrategy' that inherits from 'bt.Strategy'.
class RSIStrategy(bt.Strategy):
    def __init__(self):
        # Calculate the 14-period RSI using 'talib' on the provided data and store it in 'self.rsi'.
        self.rsi = bt.talib.RSI(self.data, timeperiod=14)

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.buy(size=1)
        else:
            if self.rsi > 70:
                self.close()

# Create an instance of the 'Cerebro' class, used for backtesting.
cerebro = bt.Cerebro()


fromdate = datetime.datetime.strptime('2020-07-01','%Y-%m-%d')
todate = datetime.datetime.strptime('2020-07-12','%Y-%m-%d')




# Load historical data and trade on 15MIN timeframe. Zoom on fromdate to startdate
data = bt.feeds.GenericCSVData(dataname='BTC_data.csv', dtformat=2, compression=15, timeframe = bt.TimeFrame.Minutes, fromdate= fromdate, todate=todate)

# Add the historical data to the 'Cerebro' instance for analysis.
cerebro.adddata(data)

# # Add the 'RSIStrategy' to the 'Cerebro' instance to be used in the backtest.
cerebro.addstrategy(RSIStrategy)

# Execute the backtest.
cerebro.run()

# Display a plot of the backtest results.
cerebro.plot()
