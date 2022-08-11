import streamlit as st
import plotly.express as px
import plotly.io as pio
import subprocess
import pyautogui
import os

def close_window():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    print("close_window")
    os._exit(0)
    st.stop()

# data
data = px.data.iris()

# sidemenu
st.sidebar.markdown(
    "# Qiita sample"
)
template = st.sidebar.selectbox(
    "Template", list(pio.templates.keys())
)

#セレクトボックスのリストを作成
pagelist = ["page1","page2"]
#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択",pagelist)
if selector=="page1":
    if st.button('ページ1ボタン'):
        st.title("ページ1のタイトル")

    # try:
    #     raise keyboardinterrupt("test_error!")
    # except keyboardinterrupt as e:
    #     print(e)

elif selector=="page2":
    if st.button('ページ2ボタン'):
        st.title("ページ2のタイトル")

# body
st.write(
    px.scatter(data, x="sepal_width", y="sepal_length", template=template)
)

# 終了ボタン
if st.button('End'):
    close_window()
