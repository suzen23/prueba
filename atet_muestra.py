import numpy as np
import streamlit as st
import time
import pandas as pd
import plotly.express as px



#testing 1
st.header = ('holas')
st.write('Hello world!')


uploaded_file = st.file_uploader('Elija archivo xlsx', type='xlsx')

if uploaded_file:
  st.markdown('---')
  df = pd.read_excel(uploaded_file, engine='openpyxl')
  st.dataframe(df)



