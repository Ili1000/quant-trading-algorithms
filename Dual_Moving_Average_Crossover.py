import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock = yf.download(["NXP"], 
                    start="2022-01-01",
                    interval= "1d",
                    auto_adjust=True)

#Get the moving averages
stock["quick_MA"] = stock["Close"].rolling(20).mean()
stock["slow_MA"] = stock["Close"].rolling(50).mean()

#signals on when to buy
stock["signal"] = (stock["quick_MA"] > stock["slow_MA"]).astype(int)
stock["signal_change"] = stock["signal"].diff()

#conditions for buying and selling
stock["buy"] = (stock["signal_change"] > 0).astype(int) 
stock["sell"] = (stock["signal_change"] < 0).astype(int)

#return each closing for each method
stock["return"] = stock["Close"].pct_change()
stock["position"] = stock["signal"].shift(1)

stock["strategy_return"] = stock["position"] * stock["return"]

#cumulative return each method
stock["buy_hold"] = (
    1 + stock["return"].fillna(0)
).cumprod()

stock["strategy"] = (
    1 + stock["strategy_return"].fillna(0)
).cumprod()



stock[["buy_hold", "strategy"]].plot(   
    title="ASML: Buy & Hold vs Moving Average Strategy"
)

plt.ylabel("Growth of €1")
plt.grid(True)
plt.show()
