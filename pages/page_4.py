import streamlit as st
import pandas as pd

# データ分析
df = pd.read_csv('./data/data2.csv', index_col='日付')
st.line_chart(df)
st.bar_chart(df)


def main():
    st.title("ファイルを読み込んでデータフレームを表示する")

    # ファイル選択ダイアログボックスを表示
    file = st.file_uploader("ファイルを選択してください", type=["csv", "xlsx"])

    if file is not None:
        file_extension = file.name.split(".")[-1]

        try:
            if file_extension == "csv":
                df = pd.read_csv(file, encoding="utf-8")
            elif file_extension == "xlsx":
                df = pd.read_excel(file, engine="openpyxl")

            st.write("データフレームの内容:")
            st.dataframe(df)

        except Exception as e:
            st.error("ファイルの読み込み中にエラーが発生しました。")
            st.error(e)


if __name__ == "__main__":
    main()
