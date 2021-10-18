import yfinance as yf
import streamlit as st
from datetime import date

st.write("""
# Simple Stock Price App
Shown are the stock **opening price**, **closing price** and ***volume*** !
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
LL = ["Apple","Microsoft","NVIDIA","Adobe","IBM","Uber","Dell","Coinbase"]
L = ['AAPL','MSFT','NVDA','ADBE','IBM','UBER','DELL','COIN']
st.sidebar.title("STOCK PRICE")
Choice = st.sidebar.radio("Pick a company",LL,index=1)
Choice = L[LL.index(Choice)]
tickerSymbol = Choice
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
time1 = date.today()
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=time1)
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## Opening Price
""")
st.line_chart(tickerDf.Open)
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)


