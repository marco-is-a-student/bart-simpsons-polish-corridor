import streamlit as st
from PIL import Image
st.set_page_config(page_title="Avenger's doomsday countdown",page_icon="🤖",layout="wide")

if 'character' not in st.session_state:
    st.session_state.character = "67 kid"
if 'Avengers Doomsday' not in st.session_state:
    st.session_state.movie = "Avengers Doomsday"
st.markdown(f"""
<h1 style="font-family: 'Times New Roman'; text-align: center">
{st.session_state.movie} countdown with {st.session_state.character}
</h1>
"""
,unsafe_allow_html=True)


col1,col2,col3,col4,col5 = st.columns(5)
with col2:
    st.selectbox("Character",["67 kid","Wario","animegirl1","animegirl2","bart simpson","Frank"],key="character",width=200)
with col4:
    st.selectbox("Movie",["Avengers Doomsday","thats all"],key="movie",width=200)
    toasty = st.button("click here to toast")
    if toasty:
        st.toast("### HIIIIII",duration="short")
with col3:
    if st.session_state.character == "67 kid":
        st.image("./images/67kid.jpeg")
    elif st.session_state.character == "Wario":
        img2 = Image.open("./images/Wario.png")
        resized = img2.resize((300,150))
        st.image(resized)
    elif st.session_state.character == "animegirl1":
        st.image("./images/animegirl1.jpg")
    elif st.session_state.character == "animegirl2":
        img2 = Image.open("./images/animegirl2.webp")
        resized = img2.resize((200,350))
        st.image(resized)
    elif st.session_state.character == "bart simpson":
        img2 = Image.open("./images/emobart.jpg")
        resized = img2.resize((200,350))
        st.image(resized)
    elif st.session_state.character == "Frank":
        st.image("./images/IMG_2373.jpg")
