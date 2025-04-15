import yfinance as yf
import time
import pandas as pd
import matplotlib.pyplot as plt

trading_symbol = "AAPL"

plt.ion()  # Turn on interactive mode

while True:
    stock = yf.Ticker(trading_symbol)
    historical_data = stock.history(period="30d", interval="1d")
    closing_prices = historical_data["Close"]

    # Plot
    plt.clf()  # Clear previous plot
    plt.plot(closing_prices.index, closing_prices.values, marker='o', linestyle='-')
    plt.title(f"{trading_symbol} - Last 30 Days Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.pause(0.1)  # Briefly pause to show the plot

    print(f"Updated: {closing_prices.index[-1]} | Current Price: {closing_prices.iloc[-1]}")

    time.sleep(30)  # Wait 30 seconds before the next refresh

import streamlit as st
import yfinance as yf
import pandas as pd
import time

# Title
st.title("📈 Live Stock Price Dashboard")

# Ticker selection
ticker = st.text_input("AAPL")

# Fetch data
@st.cache_data(ttl=30)
def get_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="30d", interval="1d")
    return data["Close"]

# Auto-refresh every 30 seconds
placeholder = st.empty()

while True:
    with placeholder.container():
        closing_prices = get_data(ticker)
        st.line_chart(closing_prices)
        st.write(f"**Last updated:** {closing_prices.index[-1].strftime('%Y-%m-%d')} | **Current price:** {closing_prices.iloc[-1]:.2f} USD")

    time.sleep(30)

#run on your terminal = streamlit run stock_dashboard.py
