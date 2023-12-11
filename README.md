# [KOREAN README](https://github.com/juho-creator/Crypto_AlgoTrading/blob/master/README%20(KR).md)


# Crypto AlgoTrading
- Following was developed based on code from  [Binance API Tutorial series by Part Time Larry](https://www.youtube.com/watch?v=rvhnz1yBHgQ&list=PLvzuUVysUFOuB1kJQ3S2G-nB7_nHhD7Ay)
- After collecting BTC price data, you could backtest and forward test based on RSI strategy
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
</br></br></br>

## Must Work on
- [X] [Collecting Fear & Greed Index](https://github.com/juho-creator/fear_greed/blob/main/dataCreator.py)
- [ ] Creating trading strategy based on Fear & Greed Index
- [ ] Back/forwardtesting Fear & Greed Index trading strategy

As I study more about crypto market and algotrading, it seems like there's alot of requirement for guaranteed profits. </br>
Currently I'm creating crypto arbitrage trading algorithm to generate profit (personal project - Not shared yet)
I will come back to this project for additional profits. 

The reason for doing so is :
- Algorthmic trading doesn't generate any profit until a profitable strategy is found
- Arbitrage trading provides guaranteed profits if the program could detect price difference across exchanges and quickly transfer crypto and sell at a higher price.


