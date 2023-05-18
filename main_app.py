from PIL import Image
import streamlit as st

st.title('開発中')
st.caption('これは丸尾将満のサイトです。')
image = Image.open('./data/img.png')
st.image(image, width=100)
