import streamlit as st
import sys
import os
import subprocess
import pyautogui


def close_window():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    print("aaaaa")
    os._exit(0)
    st.stop()

def app():

    if "count" not in st.session_state:
        st.session_state.count = 0
    else:
        close_window()

    st.title('またまたこんにちは, 世界！！')
    st.write('ねこはとてもかわいい')

    # 終了ボタン
    if st.button('End'):
        close_window()



