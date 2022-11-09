# Librerias y dependencias
import ccxt
import pandas as pd 
import numpy as np

# Consumo de datos
## Exchange Crypto
def f_crypto(coin):
    crypto = ccxt.cryptocom()
    crypto_time_samp = crypto.iso8601(crypto.milliseconds())
    crypto_btc_ob = crypto.fetch_order_book(coin, limit=30)
    crypto_btc_ob_ask = pd.DataFrame(crypto_btc_ob['asks'], columns = ['price','quantity'])
    crypto_btc_ob_bid = pd.DataFrame(crypto_btc_ob['bids'], columns = ['price','quantity'])
    crypto_bid = crypto_btc_ob['bids'][0][0] if len (crypto_btc_ob['bids']) > 0 else None
    crypto_ask = crypto_btc_ob['asks'][0][0] if len (crypto_btc_ob['asks']) > 0 else None
    crypto_bid_volume = crypto_btc_ob['bids'][0][1] if len (crypto_btc_ob['bids']) > 0 else None
    crypto_ask_volume = crypto_btc_ob['asks'][0][1] if len (crypto_btc_ob['asks']) > 0 else None
    crypto_spread = (crypto_ask - crypto_bid) if (crypto_bid and crypto_ask) else None
    crypto={
        'Timestamp':crypto_time_samp,
            'Ask': crypto_ask,
            'Bid': crypto_bid,
            'Ask Volume': crypto_ask_volume,
            'Bid Volume': crypto_bid_volume,
            'Spread': crypto_spread,
            'Close Price': 0
    }
    return(crypto)
## Exchange Bitmex
def f_bitmex(coin):
    bitmex = ccxt.bitmex()
    bitmex_time_samp = bitmex.iso8601(bitmex.milliseconds())
    bitmex_btc_ob = bitmex.fetch_order_book(coin, limit=30)
    bitmex_btc_ob_ask = pd.DataFrame(bitmex_btc_ob['asks'], columns = ['price','quantity'])
    bitmex_btc_ob_bid = pd.DataFrame(bitmex_btc_ob['bids'], columns = ['price','quantity'])
    bitmex_bid = bitmex_btc_ob['bids'][0][0] if len (bitmex_btc_ob['bids']) > 0 else None
    bitmex_ask = bitmex_btc_ob['asks'][0][0] if len (bitmex_btc_ob['asks']) > 0 else None
    bitmex_bid_volume = bitmex_btc_ob['bids'][0][1] if len (bitmex_btc_ob['bids']) > 0 else None
    bitmex_ask_volume = bitmex_btc_ob['asks'][0][1] if len (bitmex_btc_ob['asks']) > 0 else None
    bitmex_spread = (bitmex_ask - bitmex_bid) if (bitmex_bid and bitmex_ask) else None
    bitmex={
        'Timestamp':bitmex_time_samp,
            'Ask': bitmex_ask,
            'Bid': bitmex_bid,
            'Ask Volume': bitmex_ask_volume,
            'Bid Volume': bitmex_bid_volume,
            'Spread': bitmex_spread,
            'Close Price': 0
    }
    return(bitmex)
## Exchange Bitso
def f_bitso(coin):
    bitso = ccxt.bitso()
    bitso_time_samp = bitso.iso8601(bitso.milliseconds())
    bitso_btc_ob = bitso.fetch_order_book(coin, limit=30)
    bitso_btc_ob_ask = pd.DataFrame(bitso_btc_ob['asks'], columns = ['price','quantity'])
    bitso_btc_ob_bid = pd.DataFrame(bitso_btc_ob['bids'], columns = ['price','quantity'])
    bitso_bid = bitso_btc_ob['bids'][0][0] if len (bitso_btc_ob['bids']) > 0 else None
    bitso_ask = bitso_btc_ob['asks'][0][0] if len (bitso_btc_ob['asks']) > 0 else None
    bitso_bid_volume = bitso_btc_ob['bids'][0][1] if len (bitso_btc_ob['bids']) > 0 else None
    bitso_ask_volume = bitso_btc_ob['asks'][0][1] if len (bitso_btc_ob['asks']) > 0 else None
    bitso_spread = (bitso_ask - bitso_bid) if (bitso_bid and bitso_ask) else None
    bitso={
        'Timestamp':bitso_time_samp,
            'Ask': bitso_ask,
            'Bid': bitso_bid,
            'Ask Volume': bitso_ask_volume,
            'Bid Volume': bitso_bid_volume,
            'Spread': bitso_spread,
            'Close Price': 0
    }
    return(bitso)

## crypto
f_crypto('USDT')
f_crypto('DOGE')
f_crypto('CRO')
## bitmex
f_bitmex('XBTUSD')
f_bitmex('DOGEUSD')
f_bitmex('APEUSDT')
## bitso
f_crypto('BTC')
f_crypto('DOGE')
f_crypto('SHIB')

# Visualizacion de Microestructura
df=pd.DataFrame()
df['exchange']=[1]
df['timeStamp']=[1]
df['level']=[1]
df['ask_volume']=[1]
df['bid_volume']=[1]
df['total_volume']=[1]
df['mid_price']=[1]
df['vwap']=[1]
# Modelado de Microestructura
df2=pd.DataFrame()
df2['timestamp']=[1]
df2['Close']=[1]
df2['Spread']=[1]
df2['Effective Spread']=[1]