from flask import Flask,render_template,request,flash,redirect,jsonify
from config import API_KEY,API_SECRET 
import AlgoTrading as  AT
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import time

current_time = str(int(time.time()))


client = Client(API_KEY, API_SECRET)


app = Flask(__name__)

balances = AT.balance()
symbols = AT.all_symbols()



@app.route("/")
def index():
    title = 'CoinView'

    return render_template('index.html',title=title,my_balance=balances,symbols=symbols)


@app.route("/buy",methods=['POST'])
def buy():    
    try:
        quantity = request.form['quantity']
        symbol = request.form['symbol']
        order = AT.buy(symbol,quantity)
        return redirect('/')

    except Exception as e:
        return 'error'
    

@app.route("/history")
def history():    
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1698418800", current_time)
    
    processed_candlesticks = []

    for data in candlesticks:
        candlestick=	{
             'time': data[0] / 1000, 
             'open': data[1], 
             'high': data[2], 
             'low': data[3],
            'close': data[4]
            }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)




if __name__=='__main__':
    app.run(debug=True, port=4000)