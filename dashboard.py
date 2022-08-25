import streamlit as st 
import yfinance as yf
import pandas as pd

# import csv

st.title("Stock Comparison Dashboard")

#tickers = ('TSLA', 'AAPL', 'MSFT', 'GOOG', 'AMZN', 'META', 'V', 'NVDA', 'UNH' 'TSM', 'JNJ', 'XOM', 'WMT', 'PG', 'JPM', 'BAC', 'MA', )
tickers = ('BTC-USD', 'GBP=X')

st.write("With support for over 20 stocks, the Stock Comparsion Dashboard can graph multiple stocks' cumulative and relative returns.")

dropdown = st.multiselect('Pick your stocks', tickers)

#change to last years's date
start = st.date_input('Start Date', value = pd.to_datetime('01/01/2022'))
end = st.date_input('End Date', value = pd.to_datetime('today'))

def relativeReturns(df):
    rel = df.pct_change()
    cumulRet = (1+rel).cumprod() - 1
    cumulRet = cumulRet.fillna(0)
    return cumulRet

if len(dropdown) == 1:
    df1 = yf.download(dropdown, start, end) ['Adj Close']
    st.header("Cumulative Returns of {}".format(dropdown))
    st.write("Cumulative returns are the total change in the stock price between the selected start and end date. Although this visualizes the change in stock price, relative returns are more useful for comparing the performance of multiple stocks.")
    st.line_chart(df1)
    df = relativeReturns(yf.download(dropdown, start, end) ['Adj Close'])
    
    st.header("Relative Returns of {}".format(dropdown))
    st.write("Relative returns present the returns on an investment compared to a benchmark. Because the data are on the same axis, the Relative Returns graph makes comparing perfomances of multiple stocks easier.")
    st.line_chart(df)

if len(dropdown) > 1:
    #df = yf.download(dropdown, start, end) ['Adj Close']
    
    df = relativeReturns(yf.download(dropdown, start, end) ['Adj Close'])
    st.header("Relative Returns of {}".format(dropdown))
    st.write("Relative returns present the returns on an investment compared to a benchmark. Because the data are on the same axis, the Relative Returns graph makes comparing perfomances of multiple stocks easier.")
    st.line_chart(df)

    # Splits dropdown into 2 lists: 1 with the first term and 1 with the second term until the end. 
    # This is so that the first term can have the text about cumulative returns

    d1 = dropdown[1:]
    d0 = dropdown[0]
    df1 = yf.download(d0, start, end) ['Adj Close']
    st.header("Cumulative Returns of {}".format(d0))
    st.write("Cumulative returns are the total change in the stock price between the selected start and end date. Although this visualizes the change in stock price, relative returns are more useful for comparing the performance of multiple stocks.")
    st.line_chart(df1)

    for i in d1:
        df1 = yf.download(i, start, end) ['Adj Close']
        st.header("Cumulative Returns of {}".format(i))
        st.line_chart(df1)
    
        
    

#notes for tomorrow: check st and yf documentation for info about stocks details (+/- whatever), add header/subtitle w more info
