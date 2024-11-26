import streamlit as st
import pandas as pd

st.title('GoData Vehicle Classifier')

st.info('This app builds a machine learining model')
df = pd.read_csv('https://drive.google.com/file/d/1DbHYq82ZemRz6etqJ_bq5jZRsHi4iytP/view?usp=drive_link')
df
