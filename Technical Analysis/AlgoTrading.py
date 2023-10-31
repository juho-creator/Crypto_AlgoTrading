
import ccxt
from pprint import pprint
import config

binance = ccxt.binance({
    'apiKey': config.API_KEY,
    'secret': config.API_SECRET,
    'enableRateLimit': True,  # https://github.com/ccxt/ccxt/wiki/Manual#rate-limit
    'options': {
        'defaultType': 'future',
        'adjustForTimeDifference': True,
    },
})

binance.set_sandbox_mode(True)  # comment if you're not using the testnet
# binance.verbose = True  # debug output


# Print your account balance
def balance():
    account_balance = binance.fetch_balance()
    return account_balance['total']


def all_symbols():
    symbols = binance.fapiPublicGetExchangeInfo()
    all_binance_testnet_futures_symbols = [symbol['symbol'] for symbol in symbols['symbols']]

    return all_binance_testnet_futures_symbols




# Setting leverage
def leverage(n):
    binance.set_leverage(n,"BTC/USDT")


# Buy with TPSL
def tpsl(symbol,price,quantity):
    orders = [None] * 3

    # limit price
    orders[0] = binance.create_order(
        symbol=symbol,
        type="LIMIT",
        side="buy",
        amount=quantity,
        price=price
    )

    # take profit
    orders[1] = binance.create_order(
        symbol=symbol,
        type="TAKE_PROFIT",
        side="sell",
        amount=quantity,
        price=price+3000,
        params={'stopPrice': price+2000}
    )

    # stop loss
    orders[2] = binance.create_order(
        symbol=symbol,
        type="STOP",
        side="sell",
        amount=quantity,
        price=price-3000,
        params={'stopPrice': price-2000}
    )

    for order in orders:
        pprint(order)



def buy(symbol, quantity):
    order = binance.create_market_buy_order(symbol, quantity)
    return order
