import functions as fn
import visualizations as v

# 1. Consumir datos de CCXT
m1=fn.f_consumo_datos('cryptocom','BTC/USDT')
m2=fn.f_consumo_datos('cryptocom','DOGE/USDT')
m3=fn.f_consumo_datos('cryptocom','ETH/USDT')
m4=fn.f_consumo_datos('bitso','BTC/USDT')
m5=fn.f_consumo_datos('bitso','DOGE/USD')
m6=fn.f_consumo_datos('bitso','ETH/USD')
m7=fn.f_consumo_datos('bitget','BTC/USDT')
m8=fn.f_consumo_datos('bitget','DOGE/USDT')
m9=fn.f_consumo_datos('bitget','ETH/USDT')
d=fn.f_diccionario(m1,m2,m3,m4,m5,m6,m7,m8,m9)
# 2. Visualización de Microestructura
s1=fn.f_consumo_datos_2('cryptocom',m1)
s2=fn.f_consumo_datos_2('cryptocom',m2)
s3=fn.f_consumo_datos_2('cryptocom',m3)
s4=fn.f_consumo_datos_2('bitso',m4)
s5=fn.f_consumo_datos_2('bitso',m5)
s6=fn.f_consumo_datos_2('bitso',m6)
s7=fn.f_consumo_datos_2('bitget',m7)
s8=fn.f_consumo_datos_2('bitget',m8)
s9=fn.f_consumo_datos_2('bitget',m9)
vm=fn.f_visualizacion_microestructura(s1,s2,s3,s4,s5,s6,s7,s8,s9)
g1=v.f_grafica(s1,s2,s3,s4,s5,s6,s7,s8,s9)
# 3. Modelado de Microestructura
mm=fn.f_modelado_microestructura(m1,m2,m3,m4,m5,m6,m7,m8,m9,vm)