import streamlit as st
from PIL import Image
import io

# Streamlitアプリのタイトル
st.title("画像の縮小と品質調整")

# 画像のアップロード
uploaded_image = st.file_uploader("画像をアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # 画像をPIL形式に変換
    image = Image.open(uploaded_image)
    
    # 縮小比率のスライダー
    scale_factor = st.slider("縮小比率", 0.1, 1.0, 0.5)
    
    # 画質のスライダー
    quality = st.slider("画質 (1-100)", 1, 100, 95)
    
    # 画像を縮小
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    resized_image = image.resize((new_width, new_height))
    
    # 画像をJPEG形式で保存
    output = io.BytesIO()
    resized_image.save(output, format="JPEG", quality=quality)
    output.seek(0)
    
    # 処理後の画像を表示
    st.image(output, caption="処理後の画像", use_column_width=True)
    