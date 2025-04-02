import streamlit as st

# Page configuration
st.set_page_config(
    layout="wide"
)

# メインタイトルと説明
st.title("Streamlitデスクトップアプリの例")

# サイドバーの設定オプション
with st.sidebar:
    st.header("設定")
    show_data = st.checkbox("サンプルデータを表示", True)

# インタラクティブな要素
col1, col2 = st.columns(2)

with col1:
    st.subheader("インタラクティブコンポーネント")
    name = st.text_input("名前を入力してください", "ゲスト")
    age = st.slider("年齢を選択してください", 0, 100, 25)
    if st.button("挨拶する"):
        st.success(f"こんにちは {name} さん！あなたは {age} 歳です。")

with col2:
    st.subheader("データの可視化")
    if show_data:
        import pandas as pd
        import numpy as np
        
        # Create sample data
        data = pd.DataFrame({
            'x': range(10),
            'y': np.random.randn(10)
        })
        
        # Display as chart
        st.line_chart(data.set_index('x'))
        
        # Display as table
        st.dataframe(data)


# 自作モジュールの呼び出し
from util.custom_module import test_function
st.subheader("自作モジュールの呼び出し")
st.success(test_function())


# Streamlitのサードパーティコンポーネント
from streamlit_image_comparison import image_comparison
from PIL import Image
st.subheader("Streamlitのサードパーティコンポーネント")
image_comparison(
    img1=Image.open("./app/data/image1.png"),
    img2=Image.open("./app/data/image2.png"),
    in_memory=True,
)

# アプリ実行時のカレントディレクトリを取得
import os
st.subheader("カレントディレクトリの取得")
if st.button("カレントディレクトリを表示"):
    current_directory = os.getcwd()
    st.write(f"カレントディレクトリ: {current_directory}")
