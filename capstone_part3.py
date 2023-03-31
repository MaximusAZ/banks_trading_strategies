# (C)Copyright 2023-2024, Danny Watkins
# All rights reserved.
'''
*******************************************************************************************
                  
@File     :   capstone_part3.py
@Time     :   03/10/2023 13:24:48
@Author   :   Danny Watkins 
@Version  :   1.0
@Contact  :   maximus@arizona.edu
@Message  :   Technical Analysis
                  
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

#PART 3: Technical Analysis

#TASK 1: Using only BAC stock, create a plot showing the Adj Close Price along with the 60 day moving average 
# of the price on the same plot
plt.figure(figsize=(8,3),dpi=150)
BAC['Adj Close'].rolling(window=60).mean().plot(label='60 Day MA') #60 day moving average (rolling is for the moving part and window is set up by days so we can set it equal to 0)
BAC['Adj Close'].plot(label='Adj Close')
plt.legend()
#plt.show()  

#BONUS TASK: Create Bollinger Bands
# *Bollinger Bands are a type of statistical chart characterizing the prices and volatility over time of a
# financial instrument or commodity, using a formulaic method propounded by John Bollinger in the 1980s.

#TASK: Create a plot which has the Adj Close price and the upper and lower bollinger bands. Use the formula
# above, with N=20 days for the rolling rate of the moving average K=2 for the multiplication of the std dev
fig,ax = plt.subplots(figsize=(8,3),dpi=200)
BAC['MA'] = BAC['Adj Close'].rolling(20).mean()    #Moving Average
BAC['STD'] = BAC['Adj Close'].rolling(20).std()    #Standard Deviation
BAC['BOL_LOWER'] = BAC['MA'] - 2*BAC['STD']        #Lower Bollinger Band (MA - K*StdDev)
BAC['BOL_UPPER'] = BAC['MA'] + 2*BAC['STD']        #Upper Bollinger Band (MA + K*StdDev)

#plot them out in a list
BAC[['Adj Close','BOL_LOWER','BOL_UPPER']].plot(ax=ax)
plt.show()