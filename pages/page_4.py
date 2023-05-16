import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#データ分析
df=pd.read_csv('./data/data2.csv',index_col='日付')
st.line_chart(df)
st.bar_chart(df)
#matplotlib
fig,ax=plt.subplots()
ax.plot(df.index,df['終値'])
ax.set_title('matplotlib')
st.pyplot(fig)