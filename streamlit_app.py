import streamlit as st
import pandas as pd

st.title('GoData Vehicle Classifier')

st.info('This app builds a machine learining model')
df = pd.read_csv('https://github.com/giftajayi/GoData-Project/blob/main/compressed_data.csv.gz')
df
