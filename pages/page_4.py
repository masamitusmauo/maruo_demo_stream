import streamlit as st
import pandas as pd
import PyPDF2
import openpyxl

# データ分析
df = pd.read_csv('./data/data2.csv', index_col='日付')
st.line_chart(df)
st.bar_chart(df)

# ファイルアップロードのプロンプトを作成
uploaded_file = st.file_uploader("Choose a PDF file", type='pdf')

if uploaded_file is not None:
    # PDFファイルを読み込む
    pdf_reader = PdfReader(uploaded_file)

    # ページ数を取得
    total_pages = len(pdf_reader.pages)

    # 各ページを読み込み、テキストとして表示
    for page in pdf_reader.pages:
        text = page.extract_text()
        st.text(text)
def main():
    st.title("ファイルを読み込んでデータフレームを表示する")

    # ファイル選択ダイアログボックスを表示
    file = st.file_uploader("ファイルを選択してください", type=["csv", "xlsx"])

    if file is not None:
        file_extension = file.name.split(".")[-1]

        try:
            if file_extension == "csv":
                df2 = pd.read_csv(file, encoding="utf-8")
            elif file_extension == "xlsx":
                df2 = pd.read_excel(file)  # , encoding="openpyxl")

            st.write("データフレームの内容:")
            st.dataframe(df2)

        except Exception as e:
            st.error("ファイルの読み込み中にエラーが発生しました。")
            st.error(e)


if __name__ == "__main__":
    main()
