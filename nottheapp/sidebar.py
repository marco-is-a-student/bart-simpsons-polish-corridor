import streamlit as st

st.set_page_config(page_title='Sidebar Demo', page_icon='🧭', layout='centered')

st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'About'])
theme_color = st.sidebar.color_picker('Pick a theme color', '#2E86C1')

st.markdown(f'<h1 style="color:{theme_color}">Sidebar Demo</h1>', unsafe_allow_html=True)

if page == 'Home':
    st.write('Welcome to the home page!')
else:
    st.write('This is the about page.')

st.caption('Run: streamlit run app_09_sidebar.py')