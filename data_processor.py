import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock = yf.download(["ASML.AS"], 
                    start="2022-01-01",
                    auto_adjust=True)

#calculate revenue: r = close/open - 1
daily_return = stock["Close"].pct_change()

print(stock.head())

#calculate the average and standard deviaton of revenue
average_daily_return = daily_return.mean()
standard_deviation = daily_return.std()

#plot
plt.plot(stock.index, stock["Close"], label = "ASML")
plt.title("ASML closin price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()