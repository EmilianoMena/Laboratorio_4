# Librerias y dependencias
import plotly.graph_objects as go
import plotly.express as px

def f_grafica(s1,s2,s3,s4,s5,s6,s7,s8,s9):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=s1['Mid_Price'], y=s1['Timestamp'], name=s1['Exchange'][1],
                            line=dict(color='blue', width=4)))
    fig.add_trace(go.Scatter(x=s2['Mid_Price'], y=s2['Timestamp'], name=s2['Exchange'][1],
                            line=dict(color='black', width=4)))
    fig.add_trace(go.Scatter(x=s3['Mid_Price'], y=s3['Timestamp'], name=s3['Exchange'][1],
                            line=dict(color='red', width=4)))
    fig.add_trace(go.Scatter(x=s4['Mid_Price'], y=s4['Timestamp'], name=s4['Exchange'][1],
                            line=dict(color='green', width=4)))
    fig.add_trace(go.Scatter(x=s5['Mid_Price'], y=s5['Timestamp'], name=s5['Exchange'][1],
                            line=dict(color='yellow', width=4)))
    fig.add_trace(go.Scatter(x=s6['Mid_Price'], y=s6['Timestamp'], name=s6['Exchange'][1],
                            line=dict(color='orange', width=4)))
    fig.add_trace(go.Scatter(x=s7['Mid_Price'], y=s7['Timestamp'], name=s7['Exchange'][1],
                            line=dict(color='pink', width=4)))
    fig.add_trace(go.Scatter(x=s8['Mid_Price'], y=s8['Timestamp'], name=s8['Exchange'][1],
                            line=dict(color='gray', width=4)))
    fig.add_trace(go.Scatter(x=s9['Mid_Price'], y=s9['Timestamp'], name=s9['Exchange'][1],
                            line=dict(color='lightseagreen', width=4)))


    # Edit the layout
    fig.update_layout(title='Gráfica: Mid_Price',
                    xaxis_title='Timestamp',
                    yaxis_title='Mid_Price')
    return fig