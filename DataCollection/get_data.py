import csv
import datetime
from binance import Client
import config


def fetch_and_save_candlestick_data(symbol, interval, start_date, end_date, output_file):
    # Initialize Binance client
    client = Client(config.API_KEY, config.API_SECRET)

    # Get candlestick data
    candles = client.get_historical_klines(symbol, interval, start_date, end_date)

    # Open CSV file
    with open(output_file, 'w', newline='') as csvfile:
        candlestick_writer = csv.writer(csvfile, delimiter=',')

        # Write header
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

        # Write candlestick data
        for candlestick in candles:
            timestamp = candlestick[0] / 1000
            dt_object = datetime.datetime.fromtimestamp(timestamp)
            formatted_date = dt_object.strftime('%Y-%m-%d')
            candlestick[0] = formatted_date
            candlestick_writer.writerow(candlestick)


# Example usage:
fetch_and_save_candlestick_data("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "31 Oct, 2023", "BTC_data.csv")
