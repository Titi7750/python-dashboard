import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

title = "<center><h1>Ventes téléphone dashboard</h1></center>"

dataframe = pd.read_excel('ventes_smartphones.xlsx')
dataframe.columns = dataframe.columns.str.strip()
dataframe = dataframe.drop(0)

dataframe_groupby_retailer = dataframe['Retailer'].groupby(dataframe['Retailer']).sum().index
dataframe_groupby_month = dataframe['InvoiceDate'].groupby(dataframe['InvoiceDate']).sum().index

col1, col2, col3 = st.columns([0.1, 0.45, 0.45])
col4, col5 = st.columns([0.50, 0.50])

with col1:
    st.date_input('Date', value=pd.to_datetime('today', format='%d %m %Y'))

with col2:
    fig_bar = px.bar(
        dataframe,
        x=dataframe['Retailer'],
        y=dataframe['TotalSales'],
        title='Total sales by retailer',
    )
    st.plotly_chart(fig_bar)

    with col4:
        option = st.selectbox(
            '',
            dataframe_groupby_retailer,
            index=None,
            placeholder='Select a retailer'
        )

        button_get_data_retailer = st.button('Get data', key='retailer')

with col3:
    fig_line = px.line(
        dataframe,
        x=dataframe['InvoiceDate'],
        y=dataframe['TotalSales'],
        title='Total sales Over Time',
    )
    st.plotly_chart(fig_line)
    
    with col5:
        option = st.selectbox(
            '',
            dataframe_groupby_month,
            index=None,
            placeholder='Select a month'
        )

        button_get_data_month = st.button('Get data', key='month')
        
st.markdown(
    '<style>.stVerticalBlock.st-emotion-cache-1it2min.e6rk8up3 {display: block ruby}</style>',
    unsafe_allow_html=True
)
