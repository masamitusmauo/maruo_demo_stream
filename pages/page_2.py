import streamlit as st
import datetime
with st.form(key='profile'):  # 以下ボタンを押されないとインプットしない
    name = st.text_input('名前')
    address = st.text_input('住所')
    # セレクトボックス
    age_category = st.selectbox('年齢', ('18才未満', '18才以上'))
    # age_category=st.radio('年齢',('18才未満','18才以上'))ラジオボタン
    # チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する。')
    # スライダー
    height = st.slider('身長', min_value=110, max_value=210)
    # 日付
    stert_date = st.date_input('開始日', datetime.date(2023, 5, 10))
    # カラーピッカー
    color = st.color_picker('テーマカラー', '#00f900')
    # 複数選択
    hobby = st.multiselect('趣味', ('スポーツ', '読書', '釣り', '映画鑑賞'))
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ{name}さん{address}に送っておきました！！')
        st.text(f'年齢層（{age_category}）')
        st.text(f'趣味は{",".join(hobby)}')