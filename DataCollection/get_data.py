import config,csv
from pprint import pprint
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager


#### DISCLAIMER
##  FOLLOWING DATA IS FROM SPOT 
## MAY NOT INCLUDE THE MOST UP TO DATE DATA



client = Client(config.API_KEY, config.API_SECRET)

# Get market depth (1 Hour Candle) (9am~9am)d
candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "31 Oct 2023")

# Open CSV File
csvfile = open('BTC_data.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# Add header
candlestick_writer.writerow([
    "Kline open time",
    "Open price",
    "High price",
    "Low price",
    "Close price",
    "Volume",
    "Kline Close time",
    "Quote asset volume",
    "Number of trades",
    "Taker buy base asset volume",
    "Taker buy quote asset volume",
    "Unused field, ignore"
])

# Write information
for candlestick in candles:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)
csvfile.close()


