import streamlit as st 
import yfinance as yf
import pandas as pd

st.title("Finance Dashboard")

tickers = ('TSLA', 'AAPL', 'MSFT', 'GOOG', 'AMZN', 'META', 'V', 'NVDA')
st.write("Cumulative returns are the total change in the stock price between the selected start and end date. Although this visualizes the change in stock price, it is not useful for comparing the performance of multiple stocks")
dropdown = st.multiselect('Pick your stocks', tickers)

#change to last years's date
start = st.date_input('Start Date', value = pd.to_datetime('01/01/2022'))
end = st.date_input('End Date', value = pd.to_datetime('today'))

def relativeReturns(df):
    rel = df.pct_change()
    cumulRet = (1+rel).cumprod() - 1
    cumulRet = cumulRet.fillna(0)
    return cumulRet

#if len(dropdown) == 1:
 #   df1 = yf.download(dropdown, start, end) ['Adj Close']
    #st.header("Cumulative Returns of {}".format(dropdown))
  #  st.line_chart(df1)

if len(dropdown) > 0:
    #df = yf.download(dropdown, start, end) ['Adj Close']
    
    for i in dropdown:
        df1 = yf.download(i, start, end) ['Adj Close']
        st.header("Cumulative Returns of {}".format(i))
        st.line_chart(df1)
        
    df = relativeReturns(yf.download(dropdown, start, end) ['Adj Close'])
    st.header("Relative Returns of {}".format(dropdown))
    st.write("Relative returns present the returns on an investment compared to a benchmark. Because the data are on the same axis, the Relative Returns graph makes comparing perfomances of multiple stocks easier.")
    st.line_chart(df)

#notes for tomorrow: check st and yf documentation for info about stocks details (+/- whatever), add header/subtitle w more info
