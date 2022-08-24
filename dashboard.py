import streamlit as st 
import yfinance as yf
import pandas as pd
#import arrow as a
st.title("Finance Dashboard")

tickers = ('TSLA', 'AAPL', 'MSFT', 'GOOG', 'AMZN', 'META', 'V', 'NVDA')

dropdown = st.multiselect('Pick your stocks', tickers)

#change to last years's date
start = st.date_input('Start', value = pd.to_datetime('01/01/2022'))
end = st.date_input('Start', value = pd.to_datetime('today'))

if len(dropdown) > 0:
    df = yf.download(dropdown, start, end) ['Adj Close']
    st.line_chart(df)
