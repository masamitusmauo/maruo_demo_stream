import streamlit as st
import pandas as pd
#データ分析
df=pd.read_csv('./data/data2.csv',index_col='日付')
st.line_chart(df)
st.bar_chart(df)
