import numpy as np
import streamlit as st
import time
import pandas as pd
from st_aggrid import AgGrid

#testing 1
st.header = ('holas')
st.write('Hello world!')





@st.cache_data()
def load_data():
    data = pd.read_csv('./ListDesestimiento1.csv', parse_dates=['referenceDate'])
    return data

data = load_data()

AgGrid(data, height=400)

