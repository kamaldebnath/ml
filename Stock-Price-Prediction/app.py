from pandas_datareader import data
import yfinance as yf
import datetime
import streamlit as st

st.title("Stock Price Prediction")
stock = st.selectbox("Pick the Stock", ['TSLA', 'GOOG', 'META','BTC-USD'])

start_date, end_date = st.date_input('From'), st.date_input('to')


def get_stock_price(name, start, end):
    return yf.download(name, start = start, end=end)

st.text(f'Price table of {stock} from {start_date} to {end_date} :')
data = get_stock_price(stock, start_date, end_date)

st.table(data)