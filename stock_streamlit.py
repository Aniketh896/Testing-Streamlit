import yfinance as yf
import streamlit as st
import pandas as pd

st.write('''
# Simple Stock Price App

## Zomato Ltd.

_Aniketh Hotagi_

--- 
''')

tickerSymbol = 'ZOMATO.NS'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2021-7-25', end='2021-8-10')

st.write('''

### **Closing Price** 

''')

st.line_chart(tickerDf.Close)


st.write('''
### **Volume** 
''')

st.line_chart(tickerDf.Volume)
