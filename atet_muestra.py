import numpy as np
import streamlit as st
import time
import pandas as pd
import time

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

streamlit run main_page.py


#testing 1
st.header = ('holas')
st.write('Hello world!')

num1 =st.number_input('Introduzac un numero:')

st.write('El numero al cuadrado es ')





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
