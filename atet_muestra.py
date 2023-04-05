import numpy as np
import streamlit as st
import time
import pandas as pd
streamlit run atet_muestra.py
import time


#testing 1
st.header = ('holas')
st.write('Hello world!')

num1 =10
num2= 20

sum = num1+num2

print (sum)




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
