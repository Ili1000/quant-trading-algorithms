import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock = yf.download(["ASML.AS"], 
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

#The drawdown of the current value with respect to the highest peak that has occured before
stock["buy_hold_drawdown"] = (
    stock["buy_hold"] / stock["buy_hold"].cummax() - 1
)

stock["strategy_drawdown"] = (
    stock["strategy"] / stock["strategy"].cummax() - 1
)

#The increase in value
buy_hold_return = stock["buy_hold"].iloc[-1] - 1
strategy_return = stock["strategy"].iloc[-1] - 1


print(
    f"Buy & Hold max drawdown: "
    f"{stock['buy_hold_drawdown'].min():.2%}"
)

print(
    f"Strategy max drawdown: "
    f"{stock['strategy_drawdown'].min():.2%}"
)

stock[["buy_hold", "strategy"]].plot(   
    title="ASML: Buy & Hold vs Moving Average Strategy"
)

plt.ylabel("Price (€)")
plt.grid(True)
plt.show()
