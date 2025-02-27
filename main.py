import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout='wide')

title = "<center><h1>Ventes téléphone dashboard</h1></center>"

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
    fig_bar_retailer = px.bar(
        dataframe_filtered,
        x='Retailer',
        y='TotalSales',
        title='Total sales by retailer',
    )
    st.plotly_chart(fig_bar_retailer)

if 'selected_month' in st.session_state and st.session_state['selected_month']:
    dataframe_filtered = dataframe[
        dataframe['InvoiceDate'].dt.strftime('%Y-%m') == st.session_state['selected_month']
    ]

with col3:
    fig_line_month = px.line(
        dataframe_filtered,
        x='InvoiceDate',
        y='TotalSales',
        title='Total sales Over Time',
    )
    st.plotly_chart(fig_line_month)

st.markdown(
    '<style>.stVerticalBlock.st-emotion-cache-1it2min.e6rk8up3 {display: block ruby}</style>',
    unsafe_allow_html=True
)

# Total Sales and Units Sold by State with Bar and Line Chart & Graph Objects
fig_bar_line = go.Figure()

state_groupby = dataframe.groupby('State').agg({
    'TotalSales': 'sum',
    'UnitsSold': 'sum'
}).reset_index()

fig_bar_line.add_trace(
    go.Bar(
        x=state_groupby['State'],
        y=state_groupby['TotalSales'],
        name='Total Sales',
        marker_color='blue'
    )
)

fig_bar_line.add_trace(
    go.Scatter(
        x=state_groupby['State'],
        y=state_groupby['UnitsSold'],
        yaxis='y2',
        name='Units Sold',
        mode='lines',
        line=dict(color='orange')
    )
)

fig_bar_line.update_layout(
    title='Total Sales and Units Sold by State',
    xaxis_title='State',
    yaxis=dict(title="Total Sales", side="left"),
    yaxis2=dict(title="Units Sold", overlaying="y", side="right"),
    legend=dict(x=1, y=1),
    barmode='group'
)

st.plotly_chart(fig_bar_line)