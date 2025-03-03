# Import required libraries
import streamlit as st

st.set_page_config(page_title="Universal Converter", page_icon="🔄", layout="centered")

# page Setup
currency_converter = st.Page(
    page='pages/currency_converter.py',
    title='CurrencY Converter ',
    icon='💰',
    
   
)

unit_converter = st.Page(
    page='pages/unit_converter.py',
    title='Unit Converter',
    icon='📏',
    
)

About = st.Page(
    page='pages/About.py',
    title='About',
    icon='💬',
    default=True,
)

pg = st.navigation({
    'info': [About],
    'pages':[currency_converter, unit_converter]
    
})

st.logo('assets/123.png')
st.sidebar.text('Made with ❤️ by Kulsoom Adnan')

pg.run()


