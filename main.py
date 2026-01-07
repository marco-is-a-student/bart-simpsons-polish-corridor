import streamlit as st

st.set_page_config(page_title="Avenger's doomsday countdown",page_icon="🤖",layout="wide")

if 'character' not in st.session_state:
    st.session_state.character = "67 kid"
st.markdown(f"""
<h1 style="font-family: 'Times New Roman'; text-align: center">
avenger's doomsday countdown with {st.session_state.character}
</h1>
"""
,unsafe_allow_html=True)

col1,col2,col3,col4,col5 = st.columns(5)
with col2:
    st.selectbox("Character",["67 kid","Wario","animegirl1","animegirl2"],key="character",width=200)