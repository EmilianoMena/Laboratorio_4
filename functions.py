# Librerias y dependencias
import ccxt
import pandas as pd 
import numpy as np

# Consumir datos de CCXT
def f_consumo_datos(exchange,symbol):
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
    return(df)

def f_diccionario(m1,m2,m3,m4,m5,m6,m7,m8,m9):
    diccionario={
        'BTC/USDT':{
            'Cryptocom':m1,
            'Bitso':m4,
            'Bitget':m7,
        }, 
        'DOGE/USDT':{
            'Cryptocom':m2,
            'Bitso':m5,
            'Bitget':m8,
        },
        'ETH/USDT':{
            'Cryptocom':m3,
            'Bitso':m6,
            'Bitget':m9
        }         
    }
    return(diccionario)

# Visualizacion de Microestructura
def f_consumo_datos_2(exchange,df):
    df = df.sort_values(by=['Spread'], ascending=True)
    n=len(df)
    level = np.arange(1,n+1,1)
    df2=pd.DataFrame({
        'Exchange' : [exchange]*n,
        'Timestamp' : df['Timestamp'],
        'Level' : level,
        'Ask_Volume' : df['Ask_Volume'],
        'Bid_Volume' : df['Bid_Volume'],
        'Total_Volume' : df['Ask_Volume']+df['Bid_Volume'],
        'Mid_Price' : df['Ask']+df['Bid']/2
    })
    df2['VWAP' ]= (df['Close_Price']*df2['Total_Volume'])/df2['Total_Volume']
    return(df2)

def f_visualizacion_microestructura(s1,s2,s3,s4,s5,s6,s7,s8,s9):
    df=pd.concat([s1,s2,s3,s4,s5,s6,s7,s8,s9])
    return (df)

# Modelado de Microestructura
def f_modelado_microestructura(m1,m2,m3,m4,m5,m6,m7,m8,m9,df):
    c1 = m1['Close_Price'].values.tolist()
    c2 = m2['Close_Price'].values.tolist()
    c3 = m3['Close_Price'].values.tolist()
    c4 = m4['Close_Price'].values.tolist()
    c5 = m5['Close_Price'].values.tolist()
    c6 = m6['Close_Price'].values.tolist()
    c7 = m7['Close_Price'].values.tolist()
    c8 = m8['Close_Price'].values.tolist()
    c9 = m9['Close_Price'].values.tolist()
    s1 = m1['Spread'].values.tolist()
    s2 = m2['Spread'].values.tolist()
    s3 = m3['Spread'].values.tolist()
    s4 = m4['Spread'].values.tolist()
    s5 = m5['Spread'].values.tolist()
    s6 = m6['Spread'].values.tolist()
    s7 = m7['Spread'].values.tolist()
    s8 = m8['Spread'].values.tolist()
    s9 = m9['Spread'].values.tolist()
    df2=pd.DataFrame()
    df2['Timestamp']=df['Timestamp']
    df2['Close'] = c1+c2+c3+c4+c5+c6+c7+c8+c9
    df2['Spread'] = s1+s2+s3+s4+s5+s6+s7+s8+s9
    #df2['Effective Spread']=[1]
    return(df2)