# Librerias y dependencias
import ccxt
import pandas as pd 
import numpy as np

# crypto BTC/USDC, ETH/USDC, DOGE/USDC
# bitmex DOT/USDT, APE/USDT, DOGE/USDT
# bitso BTC/MXN, ETH/BRL, DOGE/USD

def f_consumir_datos(exchange, coin):
    exchange_id = exchange
    exchange = getattr(ccxt, exchange_id)
    timestamp = exchange.iso8601(exchange.milliseconds())
    exchange_btc_ob = exchange.fetch_order_book(coin, limit=30)
    exchange_btc_ob_ask = pd.DataFrame(exchange_btc_ob['asks'], columns = ['price','quantity'])
    exchange_btc_ob_bid = pd.DataFrame(exchange_btc_ob['bids'], columns = ['price','quantity'])
    exchange_bid = exchange_btc_ob['bids'][0][0] if len (exchange_btc_ob['bids']) > 0 else None
    exchange_ask = exchange_btc_ob['asks'][0][0] if len (exchange_btc_ob['asks']) > 0 else None
    exchange_bid_volume = exchange_btc_ob['bids'][0][1] if len (exchange_btc_ob['bids']) > 0 else None
    exchange_ask_volume = exchange_btc_ob['asks'][0][1] if len (exchange_btc_ob['asks']) > 0 else None
    exchange_spread = (exchange_ask - exchange_bid) if (exchange_bid and exchange_ask) else None
    a={
        'Timestamp':[timestamp],
            'Ask': [exchange_ask],
            'Bid': [exchange_bid],
            'Ask Volume': [exchange_ask_volume],
            'Bid Volume': [exchange_bid_volume],
            'Spread': [exchange_spread],
            'Close Price': [0]
    }
    return(a)
f_consumir_datos('cryptocom','BTC/USDC')