import streamlit as st
import subprocess
import greeting1
import greeting2

PAGES = {
    "App1": greeting1,
    "App2": greeting2
}

def close_window():
    st.stop()

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    # 終了ボタン
    if st.sidebar.button('Stop'):
        close_window()

    st.title('初期ページのタイトル')
    st.write('初期ページの文言')

    page = PAGES[selection]
    page.app()

if __name__ == '__main__':
    main()
