# AlgoTrading
- This code is from [Binance API Tutorial series by Part Time Larry](https://www.youtube.com/watch?v=rvhnz1yBHgQ&list=PLvzuUVysUFOuB1kJQ3S2G-nB7_nHhD7Ay) </br>
- Code is organized with more functionality for ease of use. </br></br></br>


### Data Collection
- **get_data.py** : Create a CSV file of price history
- **back_test.py** : Backtest simple RSI strategy over price history collected from get_data.py
- **config.py** : Your Binance Credentials (API KEY)
- **wscat** : wscat command for collecting price data from binance websocket
</br></br>

### Live Chart
 - Flask for displaying live price chart for bitcoin
</br></br></br>

### Technical Analysis
- **AlgoTrading.py** : Functions for adjusting orders (TPSL, leverage) and checking remaining balance.
- **TechnicalAnalysis.py** : For checking and testing SMA and RSI values
- **bot.py** : Live trading with simple RSI strategy


