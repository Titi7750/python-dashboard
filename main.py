import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

title = "<center><h1>Ventes téléphone dashboard</h1></center>"
st.markdown(title, unsafe_allow_html=True)

dataframe = pd.read_excel('ventes_smartphones.xlsx')
dataframe.columns = dataframe.columns.str.strip()
dataframe = dataframe.drop(0)

dataframe['InvoiceDate'] = pd.to_datetime(dataframe['InvoiceDate'], errors='coerce')

dataframe_groupby_retailer = dataframe['Retailer'].unique()
dataframe_groupby_month = dataframe['InvoiceDate'].dt.strftime('%Y-%m').unique()

col1, col2, col3 = st.columns([0.1, 0.45, 0.45])
col4, col5 = st.columns([0.50, 0.50])

with col1:
    st.date_input('Date', value=pd.to_datetime('today', format='%d %m %Y'))

with col4:
    selected_retailer = st.selectbox(
        '',
        dataframe_groupby_retailer,
        index=None,
        placeholder='Select a retailer'
    )

    button_get_data_retailer = st.button('Get data', key='retailer')
    
    if button_get_data_retailer:
        st.session_state['selected_retailer'] = selected_retailer

with col5:
    selected_month = st.selectbox(
        '',
        dataframe_groupby_month,
        index=None,
        placeholder='Select a month'
    )

    button_get_data_month = st.button('Get data', key='month')
    
    if button_get_data_month:
        st.session_state['selected_month'] = selected_month

if 'selected_retailer' in st.session_state and st.session_state['selected_retailer']:
    dataframe_filtered = dataframe[dataframe['Retailer'] == st.session_state['selected_retailer']]
else:
    dataframe_filtered = dataframe

with col2:
    fig_bar = px.bar(
        dataframe_filtered,
        x='Retailer',
        y='TotalSales',
        title='Total sales by retailer',
    )
    st.plotly_chart(fig_bar)

if 'selected_month' in st.session_state and st.session_state['selected_month']:
    dataframe_filtered = dataframe[
        dataframe['InvoiceDate'].dt.strftime('%Y-%m') == st.session_state['selected_month']
    ]

with col3:
    fig_line = px.line(
        dataframe_filtered,
        x='InvoiceDate',
        y='TotalSales',
        title='Total sales Over Time',
    )
    st.plotly_chart(fig_line)

st.markdown(
    '<style>.stVerticalBlock.st-emotion-cache-1it2min.e6rk8up3 {display: block ruby}</style>',
    unsafe_allow_html=True
)
