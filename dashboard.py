import streamlit as st 
import yfinance as yf
import pandas as pd



from tickers import tickers


st.title("Stock Comparison Dashboard")


st.write("With support for stocks in the NYSE and NASDAQ, and select currency and cryptocurrency exchange rates, the Stock Comparison Dashboard graphs cumulative and relative returns.")

dropdown = st.multiselect('Pick your stocks/currencies/cryptocurrencies', tickers)


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
    st.write("Cumulative returns are the total change in price between the selected start and end date. Although this visualizes the change in stock price or currency exchange rate, relative returns are more useful for comparing the performance of multiple stocks/currencies.")
    st.line_chart(df1)
    df = relativeReturns(yf.download(dropdown, start, end) ['Adj Close'])
    
    st.header("Relative Returns of {}".format(dropdown))
    st.write("Relative returns present the returns on an investment compared to a benchmark. Because the data are on the same axis, the Relative Returns graph makes comparing perfomances of multiple stocks/currencies easier.")
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
    