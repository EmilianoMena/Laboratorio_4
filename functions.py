# Librerias y dependencias
import ccxt
import pandas as pd 
import numpy as np

# Consumir datos de CCXT
## Función para cryptocom
def cryptocom(coin):
    exchange = ccxt.cryptocom()
    exchange_ohlcv = exchange.fetch_ohlcv(coin, limit=30)
    df_exchange_ohlcv = pd.DataFrame(exchange_ohlcv)
    exchange_ob = exchange.fetch_order_book(coin, limit=30)
    df_exchange_ob = pd.DataFrame(exchange_ob)
    exchange_ob_ask = pd.DataFrame(exchange_ob['asks'], columns = ['price','quantity'])
    exchange_ob_bid = pd.DataFrame(exchange_ob['bids'], columns = ['price','quantity'])
    timestamp = df_exchange_ob['datetime']
    ask = exchange_ob_ask['price']
    bid = exchange_ob_bid['price']
    ask_volume = exchange_ob_ask['quantity']
    bid_volume = exchange_ob_bid['quantity']
    spread = ask - bid
    close_price = df_exchange_ohlcv.iloc[:,4]
    df=pd.DataFrame({
        'Timestamp':timestamp,
        'Ask':ask,
        'Bid':bid,
        'Ask_Volume':ask_volume,
        'Bid_Volume':bid_volume,
        'Spread':spread,
        'Close_Price':close_price
    })
    df=df.fillna(0)
    return(df)
## Función para bitso
def bitso(coin):
    exchange = ccxt.bitso()
    exchange_ohlcv = exchange.fetch_ohlcv(coin, limit=30)
    df_exchange_ohlcv = pd.DataFrame(exchange_ohlcv)
    exchange_ob = exchange.fetch_order_book(coin, limit=30)
    df_exchange_ob = pd.DataFrame(exchange_ob)
    exchange_ob_ask = pd.DataFrame(exchange_ob['asks'], columns = ['price','quantity'])
    exchange_ob_bid = pd.DataFrame(exchange_ob['bids'], columns = ['price','quantity'])
    timestamp = df_exchange_ob['datetime']
    ask = exchange_ob_ask['price']
    bid = exchange_ob_bid['price']
    ask_volume = exchange_ob_ask['quantity']
    bid_volume = exchange_ob_bid['quantity']
    spread = ask - bid
    close_price = df_exchange_ohlcv.iloc[:,4]
    df=pd.DataFrame({
        'Timestamp':timestamp,
        'Ask':ask,
        'Bid':bid,
        'Ask_Volume':ask_volume,
        'Bid_Volume':bid_volume,
        'Spread':spread,
        'Close_Price':close_price
    })
    df=df.fillna(0)
    return(df)
## Función para binance
def binance(coin):
    exchange = ccxt.binance()
    exchange_ohlcv = exchange.fetch_ohlcv(coin, limit=30)
    df_exchange_ohlcv = pd.DataFrame(exchange_ohlcv)
    exchange_ob = exchange.fetch_order_book(coin, limit=30)
    df_exchange_ob = pd.DataFrame(exchange_ob)
    exchange_ob_ask = pd.DataFrame(exchange_ob['asks'], columns = ['price','quantity'])
    exchange_ob_bid = pd.DataFrame(exchange_ob['bids'], columns = ['price','quantity'])
    timestamp = df_exchange_ob['datetime']
    ask = exchange_ob_ask['price']
    bid = exchange_ob_bid['price']
    ask_volume = exchange_ob_ask['quantity']
    bid_volume = exchange_ob_bid['quantity']
    spread = ask - bid
    close_price = df_exchange_ohlcv.iloc[:,4]
    df=pd.DataFrame({
        'Timestamp':timestamp,
        'Ask':ask,
        'Bid':bid,
        'Ask_Volume':ask_volume,
        'Bid_Volume':bid_volume,
        'Spread':spread,
        'Close_Price':close_price
    })
    df=df.fillna(0)
    return(df)

m1=cryptocom('BTC/USDT')
m2=cryptocom('DOGE/USDT')
m3=cryptocom('ETH/USDT')
m4=bitso('BTC/USDT')
m5=bitso('DOGE/USD')
m6=bitso('ETH/USD')
m7=binance('BTC/USDT')
m8=binance('DOGE/USDT')
m9=binance('ETH/USDT')
diccionario={
    'BTC/USDT':{
        'Cryptocom':m1,
        'Bitso':m4,
        'Binance':m7,
    }, 
    'DOGE/USDT':{
        'Cryptocom':m2,
        'Bitso':m5,
        'Binance':m8,
    },
    'ETH/USDT':{
        'Cryptocom':m3,
        'Bitso':m6,
        'Binance':m9
    }   
}

# Visualizacion de Microestructura
df=pd.DataFrame()
#df['Exchange']=
df['Timestamp']=pd.concat([m1['Timestamp'],m2['Timestamp'],m3['Timestamp'],m4['Timestamp'],m5['Timestamp'],m6['Timestamp'],m7['Timestamp'],m8['Timestamp'],m9['Timestamp']])
#df['Level']=
df['Ask_Volume']=pd.concat([m1['Ask_Volume'],m2['Ask_Volume'],m3['Ask_Volume'],m4['Ask_Volume'],m5['Ask_Volume'],m6['Ask_Volume'],m7['Ask_Volume'],m8['Ask_Volume'],m9['Ask_Volume']])
df['Bid_Volume']=pd.concat([m1['Bid_Volume'],m2['Bid_Volume'],m3['Bid_Volume'],m4['Bid_Volume'],m5['Bid_Volume'],m6['Bid_Volume'],m7['Bid_Volume'],m8['Bid_Volume'],m9['Bid_Volume']])
df['Total_Volume']=df['Ask_Volume']+df['Bid_Volume']
#df['Mid_Price']=((pd.concat([m1['Ask_Price'],m2['Ask_Price'],m3['Ask_Price'],m4['Ask_Price'],m5['Ask_Price'],m6['Ask_Price'],m7['Ask_Price'],m8['Ask_Price'],m9['Ask_Price']]))+(pd.concat([m1['Bid_Price'],m2['Bid_Price'],m3['Bid_Price'],m4['Bid_Price'],m5['Bid_Price'],m6['Bid_Price'],m7['Bid_Price'],m8['Bid_Price'],m9['Bid_Price']])))/2
#df['VWAP']=
print(df)

# Modelado de Microestructura
df2=pd.DataFrame()
df2['Timestamp']=df['Timestamp']
df2['Close']=pd.concat([m1['Close_Price'],m2['Close_Price'],m3['Close_Price'],m4['Close_Price'],m5['Close_Price'],m6['Close_Price'],m7['Close_Price'],m8['Close_Price'],m9['Close_Price']])
df2['Spread']=pd.concat([m1['Spread'],m2['Spread'],m3['Spread'],m4['Spread'],m5['Spread'],m6['Spread'],m7['Spread'],m8['Spread'],m9['Spread']])
#df2['Effective Spread']=[1]
print(df2)