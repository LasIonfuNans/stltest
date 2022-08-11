import greeting1
import greeting2
import streamlit as st

PAGES = {
    "App1": greeting1,
    "App2": greeting2
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

