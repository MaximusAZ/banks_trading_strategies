# (C)Copyright 2023-2024, Danny Watkins
# All rights reserved.
'''
*******************************************************************************************
                  
@File     :   capstone_part1.py
@Time     :   03/09/2023 18:28:28
@Author   :   Danny Watkins 
@Version  :   1.0
@Contact  :   maximus@arizona.edu
@Message  :   Returns Analysis
                  
*******************************************************************************************
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Portfolio of Bank Stocks

#Bank of America
BAC = pd.read_csv("BAC.csv",parse_dates=True,index_col='Date')
#JP Morgan
JPM = pd.read_csv("JPM.csv",parse_dates=True,index_col='Date')
#Citi Group
CITI = pd.read_csv("C.csv",parse_dates=True,index_col='Date')
#HSBC
HSBC = pd.read_csv("HSBC.csv",parse_dates=True,index_col='Date')
#Royal Bank of Canada
RY = pd.read_csv("RY.csv",parse_dates=True,index_col='Date')

#Lists & Dictionaries for convenience purposes
portfolio_list = [BAC,JPM,CITI,HSBC,RY]
portfolio_dict = {'BAC':BAC,'JPM':JPM,'CITI':CITI,'HSBC':HSBC,'RY':RY}

#############################################################################################

#PART 1: Returns Analysis

#TASK 1: What is the start date and and what is the end date for the price history of these stocks?
# *this data frame has the dates as the index so you can just grab the first and last index here
# *index is already sorted sequentially by default FYI
BAC.index.max()
BAC.index.min()
#or
BAC.index[0]
BAC.index[-1]

#TASK 2: Create a line plot showing the adjusted close prices over the last 5 years for all the stocks in the portfolio
# together on the same plot, make sure the plot has a legend
fig,ax = plt.subplots(dpi=150,figsize=(8,3))

BAC['Adj Close'].plot(ax=ax,label='BAC')   #these will all start to plot on same graph but to make sure, you can write it like
JPM['Adj Close'].plot(x=ax,label='JPM')    #JPM['Adj Close'].plot(ax=ax)
CITI['Adj Close'].plot(x=ax,label='CITI')
HSBC['Adj Close'].plot(x=ax,label='HSBC')
RY['Adj Close'].plot(x=ax,label='RY')

plt.legend()
plt.show()

#TASK 3: Create a function that takes in the Adj. Close price series and then calculate the stocks percent rise or decline
# from any set of given dates. For example,  you should be able to pass perc_calc(BAC,'2016-09-06','2021-09-03)
# and get back "Percent Change: 187.7%"
def perc_calc(ticker,start_date,end_date):

    if start_date not in ticker['Adj Close'].index:
        return f"Start Date not in index"
    if end_date not in ticker['Adj Close'].index:
        return f"End Date not in index"
    
    adj_close_start = ticker['Adj Close'][start_date]
    adj_close_end = ticker['Adj Close'][end_date]

    change = 100*(adj_close_end-adj_close_start)/adj_close_start

    return f"Percent Change: {np.round(change,2)}%"

#test perc_calc
print(perc_calc(BAC,'2016-09-06', '2021-09-03'))

#TASK 4: Create a Histogram of the daily returns for each stock in the Portfolio
plt.figure(dpi=200,figsize=(5,2))

#loop
for stock_name,stock_df in portfolio_dict.items():
    stock_df['Adj Close'].pct_change(1).hist(label=stock_name,alpha=0.3,bins=70) #alpha is transparency, pct_change(1) is ddaily returns

#legend labels
plt.legend()
plt.show()

#TASK 5: (Cumulative Returns) If you had invested $10,000 in BAC (appx 701 shares) at the start of the time series
# you would have about $28,773 at the end of the time period. Create a plot that shows the value of $10,000 BAC
# at the start of the time series and what value it would have in dollars throughout the rest of the time period.
bac_returns = BAC['Adj Close'].pct_change(1)[1:] #[1:] means to ignore the first row because there isnt a percent change in the first line
cumulative_return = (bac_returns+1).cumprod() #this would plot out if we started at $1 where we would be at today
bac_10000 = cumulative_return*10000 #adjust it for starting with $10,000
bac_10000.plot()
plt.show()

#TASk 6: Find the annualized Sharpe Ratios for each stock in the portfolio
def compute_sharpe_ratio(data,risk_free_rate=0): #set risk free rate equal to 0 here bc at the time of making this interest rates were extremely low
    mean_return = data['Adj Close'].pct_change(1).mean() #calculate your average daily return
    std = data['Adj Close'].pct_change(1).std() #calculate average std deviation
    sharpe_ratio = (mean_return-risk_free_rate)/std
    return (252**0.5)*sharpe_ratio #annualized return, square root of 252 bc there is 252 trading days x sharpe ratio

#loop print
for ticker, df in portfolio_dict.items():
    print(f"{ticker} Annualized Sharpe Ratio is: {np.round(compute_sharpe_ratio(df),2)}")