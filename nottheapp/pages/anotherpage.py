import streamlit as st

st.set_page_config(page_title="This is another page",layout="wide")
st.title("Another page")
st.write("hi another page")
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        width: 200px;
        min-width: 600px;
        max-width: 600px;
    }
</style>
""", unsafe_allow_html=True)