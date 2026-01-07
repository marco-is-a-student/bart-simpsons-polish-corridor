import streamlit as st


st.write("My name is david")
st.caption("I made the mimic")
st.error("It was difficult. To put the pieces. Together.")
tab1,tab2,tab3 = st.tabs(["tabu1","house","67"])
with tab2:
    st.write("🏡")
with tab3:
    value = st.slider("I am a slider",0,100,23)
    st.write(value)
with tab1:
    st.write("Boo!")

