import streamlit as st
import pandas as pd
import PyPDF2
import openpyxl

# データ分析
df = pd.read_csv('./data/data2.csv', index_col='日付')
st.line_chart(df)
st.bar_chart(df)

st.title("PDF Viewer")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
    num_pages = pdf_reader.numPages
    st.write(f"Number of pages: {num_pages}")

    for page_number in range(1, num_pages + 1):
        page = pdf_reader.getPage(page_number - 1)
        text = page.extractText()
        st.subheader(f"Page {page_number}")
        st.write(text)
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
