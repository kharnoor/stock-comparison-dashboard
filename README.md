# Stock Comparison Guide

![](https://img.shields.io/codefactor/grade/github/kharnoor/stock-comparison-dashboard/main)
![](https://img.shields.io/github/languages/code-size/kharnoor/stock-comparison-dashboard)
![](https://img.shields.io/github/license/kharnoor/stock-comparison-dashboard)

## About
The Stock Comparison Dashboard graphs cumulative and relative returns of over 9000 stocks listed on the NYSE (such as ORCL and JPM) and NASDAQ (such as AAPL and META), along with select currency and cryptocurrency exchange rates (such as BTC-USD and GBP-USD), to view and compare their performance over a selected time.

## Usage

Visit the [website](https://kharnoor-stock-comparison-dashboard-dashboard-l965pl.streamlitapp.com/) to use the web app. Select the stocks/currencies/cryptocurrencies, start date, and end date. Then, the graphs of their relative and cumulative returns are displayed below.

## Installation for Contributing

### Install pip
```bash
sudo apt-get install python3-pip
```
### Install Dependencies

- Pandas
```bash
pip install pandas
```
- Streamlit
```bash
pip install streamlit
```
- Yfinance
```bash
pip install yfinance
``` 
### Clone the Repository
```bash
git clone git@github.com:kharnoor/stock-comparison-dashboard.git
```
### Change the Current Working Directory to the Repository and Run the Program to View Edits
```bash
cd stock-comparison-dashboard/
streamlit run dashboard.py
```
## License

This project is licensed under the terms of the MIT License.



