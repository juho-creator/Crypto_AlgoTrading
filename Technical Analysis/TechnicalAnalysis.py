import talib
import numpy as np 

# Get closing price for 1HOUR candle (data)
def csv_close_numpy(filename):
    my_data = np.genfromtxt(filename, delimiter=',')
    close = my_data[:,4]
    return close

close = csv_close_numpy('BTC_data.csv')


# Caculate RSI15 for data
rsi = talib.RSI(close)
print(rsi)


# Caculatig SMA5 for data
moving_average = talib.SMA(close,timeperiod=5)
print("\nMA")
print(moving_average)
