import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

title = "<center><h1>Ventes téléphone dashboard</h1></center>"

col1, col2, col3 = st.columns([0.1, 0.45, 0.45])

dataframe = pd.read_excel('ventes_smartphones.xlsx')
dataframe.columns = dataframe.columns.str.strip()
dataframe = dataframe.drop(0)

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

with col3:
    fig_line = px.line(
        dataframe,
        x=dataframe['InvoiceDate'],
        y=dataframe['TotalSales'],
        title='Total sales Over Time',
    )
    st.plotly_chart(fig_line)
