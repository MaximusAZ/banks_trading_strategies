# (C)Copyright 2023-2024, Danny Watkins
# All rights reserved.
'''
*******************************************************************************************
                  
@File     :   capstone_part2.py
@Time     :   03/09/2023 18:28:51
@Author   :   Danny Watkins 
@Version  :   1.0
@Contact  :   maximus@arizona.edu
@Message  :   Volume Analysis
                  
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

#PART 2: Volume Analysis

#TASK 1: Create a plot showing the daily volume of stock traded over the time period of 5 years

#to view a stock's volume
JPM['Volume'].plot()
#plt.show()

#show the volumes for all stocks in portfolio with a for loop
plt.figure(dpi=200,figsize=(6,3))
for stock_name,stock_df in portfolio_dict.items():
    stock_df['Volume'].plot(label=stock_name)
plt.legend()
#plt.show() 

#TASK 2: Now create a similar plot as the previous one, but it should reflect the total dollar amount,
# meaning you will need to take into account the price on each day the volume was traded. Feel free to use
# Adj Close price as the consensus price for a given day
CITI['Total Dollar Volume'] = CITI['Adj Close'] * CITI['Volume'] #create a new column "Total Dollar Volume"
#use the same loop as before
plt.figure(dpi=200,figsize=(7,3))
for stock_name,stock_df in portfolio_dict.items():
    (stock_df['Volume']*stock_df['Adj Close']).plot(label=stock_name)
plt.legend(loc=(1,0.5))
plt.show() 

#TASK 3: Based on your plot above, which stock has the highest dollar value amount traded of their stock on a single day
# and what date was it? Did anything significant happen around this time period for that company?
# *the plot showed JPM had a huge volume day, to find out the exact date we do this...
JPM['Total Dollar Volume'] = JPM['Volume']*JPM['Adj Close']
JPM['Total Dollar Volume'].max() #returns 8345011203.784801 which means there was a day where
# $8,345,011,204.78 of JPM stock was traded
JPM['Total Dollar Volume'].idxmax() #this gives us the index location of that value which is a timestamp ('2021-03-19 00:00:00')
# on this date, Fed Reserve had a meeting and released new bank data as well as there was news that JPM was buying a 410 million dollar stake in a
# chinese Bank wealth business
