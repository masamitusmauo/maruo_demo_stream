import streamlit as st
from PIL import Image
with st.expander("See explanation"):
    st.write("The chart above shows some interesting insights about...")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image(
            "https://th.bing.com/th/id/R.deea3cdb2c8835c625d536bc311d940d?rik=ltSKpOrA4ZQmog&riu=http%3a%2f%2fwww.wallpaper-box.com%2fcat%2fimages%2fcat34.jpg&ehk=NELxnErlX8qHRHGncIv8CHZeoEAQSCtUg55c2TiTDDY%3d&risl=&pid=ImgRaw&r=0")

    with col2:
        st.header("A dog")
        st.image(
            "https://th.bing.com/th/id/R.94a0cbec04c4bc099d510109ab0a02cd?rik=OsU%2bHCvFfy13bg&riu=http%3a%2f%2fwww1.jpkabegami.com%2fimages3%2fwall%2f20070527%2f1920DOG_1009.jpg&ehk=BchXOmEL7D3Qgu2nXgfczyR7aaxyQy54CBAEwBey7RY%3d&risl=&pid=ImgRaw&r=0")

    with col3:
        st.header("An elephant")
        st.image("https://s.newtalk.tw/album/news/321/5dbf958cdfcb0.jpg")