# Librerias y dependencias
import plotly.graph_objects as go
import plotly.express as px

def f_grafica(c1,c2,c3,c4,c5,c6,c7,c8,c9):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=c1['Timestamp'], y=c1['Mid_Price'], name='cryptocom BTC/USDT',
                            line=dict(color='blue', width=4)))
    fig.add_trace(go.Scatter(x=c2['Timestamp'], y=c2['Mid_Price'], name='cryptocom DOGE/USDT',
                            line=dict(color='black', width=4)))
    fig.add_trace(go.Scatter(x=c3['Timestamp'], y=c3['Mid_Price'], name='cryptocom ETH/USDT',
                            line=dict(color='red', width=4)))
    fig.add_trace(go.Scatter(x=c4['Timestamp'], y=c4['Mid_Price'], name='bitso BTC/USDT',
                            line=dict(color='green', width=4)))
    fig.add_trace(go.Scatter(x=c5['Timestamp'], y=c5['Mid_Price'], name='bitso DOGE/USD',
                            line=dict(color='yellow', width=4)))
    fig.add_trace(go.Scatter(x=c6['Timestamp'], y=c6['Mid_Price'], name='bitso ETH/USD',
                            line=dict(color='orange', width=4)))
    fig.add_trace(go.Scatter(x=c7['Timestamp'], y=c7['Mid_Price'], name='bitget BTC/USDT',
                            line=dict(color='pink', width=4)))
    fig.add_trace(go.Scatter(x=c8['Timestamp'], y=c8['Mid_Price'], name='bitget DOGE/USDT',
                            line=dict(color='gray', width=4)))
    fig.add_trace(go.Scatter(x=c9['Timestamp'], y=c9['Mid_Price'], name='bitget ETH/USDT',
                            line=dict(color='lightseagreen', width=4)))

    # Edit the layout
    fig.update_layout(title='Gráfica: Mid_Price',
                    xaxis_title='Timestamp',
                    yaxis_title='Mid_Price')
    return fig