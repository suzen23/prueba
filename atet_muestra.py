import numpy as np
import streamlit as st
import time
import pandas as pd




#testing 1
st.header = ('holas')
st.write('Hello world!')


@st.experimental_memo
def get_chart_37893177():
    import plotly.graph_objects as go
    import pandas as pd

    #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
    df = pd.read_csv('https://github.com/suzen23/prueba/ListDesestimiento1.csv')

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df.NUMERO,df.NOMBRES, df.MOTIVO],
                   fill_color='lavender',
                   align='left'))
    ])


    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

