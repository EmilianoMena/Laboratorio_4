# Librerias y dependencias
import ccxt
import pandas as pd 
import numpy as np

# Obtener datos de CCXT
def f_datos(exchange,symbol):
    exchange_id = exchange
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'apiKey': 'YOUR_API_KEY',
        'secret': 'YOUR_SECRET',
    })
    exchange_ohlcv = exchange.fetch_ohlcv(symbol, limit=50)
    df_exchange_ohlcv = (pd.DataFrame(exchange_ohlcv)).fillna(0)
    exchange_ob = exchange.fetch_order_book(symbol, limit=50)
    df_exchange_ob = (pd.DataFrame(exchange_ob)).fillna(0)
    exchange_ob_ask = (pd.DataFrame(exchange_ob['asks'], columns = ['price','quantity'])).fillna(0)
    exchange_ob_bid = (pd.DataFrame(exchange_ob['bids'], columns = ['price','quantity'])).fillna(0)
    timestamps = df_exchange_ob['datetime']
    ask = exchange_ob_ask['price']
    bid = exchange_ob_bid['price']
    ask_volume = exchange_ob_ask['quantity']
    bid_volume = exchange_ob_bid['quantity']
    spread = ask - bid
    high_price = df_exchange_ohlcv.iloc[:,2]
    low_price = df_exchange_ohlcv.iloc[:,3]
    close_price = df_exchange_ohlcv.iloc[:,4]
    price = (high_price+low_price+close_price)/3
    total_volume = ask_volume+bid_volume
    mid_price = (ask+bid)/2
    vwap = (price*total_volume)/total_volume
    n=len(timestamps)
    df=pd.DataFrame({
        'Exchange':[exchange_id]*n,
        'Timestamp':timestamps,
        'Ask':ask,
        'Bid':bid,
        'Ask_Volume':ask_volume,
        'Bid_Volume':bid_volume,
        'Spread':spread,
        'Close_Price':close_price,
        'Exchange':[exchange]*n,
        'Total_Volume':total_volume,
        'Mid_Price':mid_price,
        'VWAP':vwap
    })
    df = df.sort_values(by=['Spread'], ascending=True)
    level = np.arange(1,n+1,1)
    df['Level']=level
    return(df)

# 1. Consumir datos de CCXT
def f_consumo_datos(df):
    exchange=df['Exchange'][0]
    timestamp=df['Timestamp']
    ask=df['Ask']
    bid=df['Bid']
    ask_volume=df['Ask_Volume']
    bid_volume=df['Bid_Volume']
    spread=df['Spread']
    close_price=df['Close_Price']
    lista=[]
    a=len(timestamp)
    for i in range(a):
        lista.append({
            exchange:{
                timestamp.iloc[i]:{
                    'Ask':ask.iloc[i],
                    'Bid':bid.iloc[i],
                    'Ask_Volume':ask_volume.iloc[i],
                    'Bid_Volume':bid_volume.iloc[i],
                    'Spread':spread[i],
                    'Close_Price':close_price[i]
                }
            }   
        })
    return(lista)

def f_diccionario(b1,b2,b3,b4,b5,b6,b7,b8):
    diccionario=b1+b2+b3+b4+b5+b6+b7+b8
    return(diccionario)

#2. Visualización de Microestructura
def f_datos_2(df):
    exchange=df['Exchange']
    timestamp=df['Timestamp']
    level=df['Level']
    ask_volume=df['Ask_Volume']
    bid_volume=df['Bid_Volume']
    total_volume=df['Total_Volume']
    mid_price=df['Mid_Price']
    vwap=df['VWAP']
    df2=pd.DataFrame({
        'Exchange':exchange,
        'Timestamp':timestamp,
        'Level':level,
        'Ask_Volume':ask_volume,
        'Bid_Volume':bid_volume,
        'Total_Volume':total_volume,
        'Mid_Price':mid_price,
        'VWAP':vwap
    })
    return(df2)

def f_visualizacion_microestructura(c1,c2,c3,c4,c5,c6,c7,c8,c9):
    df=pd.concat([c1,c2,c3,c4,c5,c6,c7,c8,c9])
    return (df)

# 3. Modelado de Microestructura
def f_datos_3(df):
    timestamp=df['Timestamp']
    close=df['Close_Price']
    spread=df['Spread']
    #effective_spread=
    df3=pd.DataFrame({
        'Timestamp':timestamp,
        'Close':close,
        'Spread':spread,
        #'Effective_Spread':effective_spread
    })
    return(df3)

def f_modelado_microestructura(d1,d2,d3,d4,d5,d6,d7,d8,d9):
    df=pd.concat([d1,d2,d3,d4,d5,d6,d7,d8,d9])
    return (df)