# Librerias y dependencias
import plotly.graph_objects as go
import plotly.express as px

def f_grafica(c1,c2,c3,c4,c5,c6,c7,c8,c9):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=c1['Mid_Price'], y=c1['Timestamp'], name=c1['Exchange'].iloc[0],
                            line=dict(color='blue', width=4)))
    fig.add_trace(go.Scatter(x=c2['Mid_Price'], y=c2['Timestamp'], name=c2['Exchange'].iloc[0],
                            line=dict(color='black', width=4)))
    fig.add_trace(go.Scatter(x=c3['Mid_Price'], y=c3['Timestamp'], name=c3['Exchange'].iloc[0],
                            line=dict(color='red', width=4)))
    fig.add_trace(go.Scatter(x=c4['Mid_Price'], y=c4['Timestamp'], name=c4['Exchange'].iloc[0],
                            line=dict(color='green', width=4)))
    fig.add_trace(go.Scatter(x=c5['Mid_Price'], y=c5['Timestamp'], name=c5['Exchange'].iloc[0],
                            line=dict(color='yellow', width=4)))
    fig.add_trace(go.Scatter(x=c6['Mid_Price'], y=c6['Timestamp'], name=c6['Exchange'].iloc[0],
                            line=dict(color='orange', width=4)))
    fig.add_trace(go.Scatter(x=c7['Mid_Price'], y=c7['Timestamp'], name=c7['Exchange'].iloc[0],
                            line=dict(color='pink', width=4)))
    fig.add_trace(go.Scatter(x=c8['Mid_Price'], y=c8['Timestamp'], name=c8['Exchange'].iloc[0],
                            line=dict(color='gray', width=4)))
    fig.add_trace(go.Scatter(x=c9['Mid_Price'], y=c9['Timestamp'], name=c9['Exchange'].iloc[0],
                            line=dict(color='lightseagreen', width=4)))

    # Edit the layout
    fig.update_layout(title='Gráfica: Mid_Price',
                    xaxis_title='Timestamp',
                    yaxis_title='Mid_Price')
    return fig