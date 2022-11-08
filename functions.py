import ccxt
import pandas as pd 
import numpy as np
import plotly.graph_objects as go

kraken = ccxt.kraken()
timestamp_kraken = kraken.iso8601(kraken.milliseconds())
kraken_btc_ob = kraken.fetch_order_book('BTC/USDT', limit=30)
kraken_btc_ob_ask = pd.DataFrame(kraken_btc_ob['asks'], columns = ['price','quantity'])
kraken_btc_ob_bid = pd.DataFrame(kraken_btc_ob['bids'], columns = ['price','quantity'])
bid = kraken_btc_ob['bids'][0][0] if len (kraken_btc_ob['bids']) > 0 else None
ask = kraken_btc_ob['asks'][0][0] if len (kraken_btc_ob['asks']) > 0 else None
spread = (ask - bid) if (bid and ask) else None
#exchange1={timestamp_kraken:(ask, bid, kraken_btc_ob_ask, kraken_btc_ob_bid, spread)}
print(kraken_btc_ob_ask)

ftx = ccxt.ftx()
timestamp_ftx = ftx.iso8601(ftx.milliseconds())
ftx_btc_ob = ftx.fetch_order_book('BTC/USDT', limit=30)
ftx_btc_ob_ask = pd.DataFrame(ftx_btc_ob['asks'], columns = ['price','quantity'])
ftx_btc_ob_bid = pd.DataFrame(ftx_btc_ob['bids'], columns = ['price','quantity'])

currencycom = ccxt.currencycom()
timestamp_currencycom = currencycom.iso8601(currencycom.milliseconds())
currencycom_btc_ob = currencycom.fetch_order_book('BTC/USDT', limit=30)
currencycom_btc_ob_ask = pd.DataFrame(currencycom_btc_ob['asks'], columns = ['price','quantity'])
currencycom_btc_ob_bid = pd.DataFrame(currencycom_btc_ob['bids'], columns = ['price','quantity'])

print(kraken_btc_ob,ftx_btc_ob,currencycom_btc_ob)