import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock = yf.download(["ASML.AS"], 
                    start="2022-01-01",
                    auto_adjust=True)


#calculate revenue: r = close/open - 1
daily_return = stock["Close"] / stock["Open"] - 1

print("The daily return: \n", daily_return)

#calculate the average and standard deviaton of revenue
average_daily_return = daily_return.mean()
standard_deviation = daily_return.std()

print("The standard deviation: \n", standard_deviation)

# print("The head: ")
# print(stock.head())
# print("The tail: ")
# print(stock.tail())
# print("The shape: ")
# print(stock.shape)
# print("The collumns: ")
# print(stock.columns)
# print("IDK: ")
# print(stock.isna().sum())