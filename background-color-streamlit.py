import streamlit as st

background_color = st.color_picker('Background color', '#F0F0F0')

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_color} !important;
    }}
    .stAppHeader {{
        background-color: {background_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.write('The background color is', background_color)