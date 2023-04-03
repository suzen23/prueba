import numpy as np
import streamlit as st
import time
import pandas as pd

#testing 1
st.header = ('holas')
st.write('Hello world!')


# Get some data.
data = np.random.randn(10, 2)

# Show the data as a chart.
chart = st.line_chart(data)

# Wait 1 second, so the change is clearer.
time.sleep(1)

# Grab some more data.
data2 = np.random.randn(10, 2)

# Append the new data to the existing chart.
chart.add_rows(data2)

#testing code web
st.title('DESESTIMIENTOS ATET')

DATA_URL = ('https://github.com/suzen23/prueba/ListDesestimiento1.csv')

####

df = pd.read_csv('ListDesestimiento1.csv')

print(df.to_string()) 


