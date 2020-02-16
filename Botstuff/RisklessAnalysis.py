#!/usr/bin/env python
# coding: utf-8

# In[51]:


import database_functions as db
import pandas as pd
from datetime import datetime
import discord as ds
from discord import Webhook, RequestsWebhookAdapter
import requests
import time
import os
import csv


# In[52]:


#datatest = db.contractmakerfordb()
#datatest = pd.read_csv('usethis.csv', header = 0, names = ['market_name', 'market_id', 'contract_best_buy_no_price','market_name', 'market_id', 'fine'])
#datatest.head(10)


# In[ ]:





# In[53]:


def riskless_algo():
    runtime_start = datetime.now()
    data = db.contractmakerfordb()
    #data = datatest
    goodmarkets = []
    idlist = []
    marketids = data.market_id.unique()
    for market in marketids:
        datalist = data[data.market_id == market].contract_best_buy_no_price
        prices1 = datalist.dropna()
        sum_list = prices1.sum()
        if sum_list < len(prices1):
            prices = prices1.tolist()
            prices.sort()
            marketname = data[data.market_id == market].market_name.drop_duplicates()
            finalprice = []
            for i in range (len(prices) - 1):
                finalprice.append(1)
            finalprice.append(0)
            grossprofit = []
            for i in range(len(prices)-1):
                grossprofit.append(finalprice[i] - prices[i])
                grossprofit[i] = grossprofit[i] * 0.9
            grossprofit.append(0)
            addprin = []
            for i in range(len(prices)):
                addprin.append(prices[i] + grossprofit[i])
            addprin[len(prices) - 1] = 0
            risk = (sum(addprin) - sum(prices))
            if risk > 0:
                goodmarkets.append([market, marketname.to_string(index=False), round(risk*1000)/1000, prices])
                idlist.append(market)
        else:
            None
    debuglist = goodmarkets
    runtime_end = datetime.now()
    total_runtime = runtime_end-runtime_start
    return goodmarkets, debuglist, idlist, total_runtime


# In[54]:


def riskless_internal():
    markets, debuglist, idlist, total_runtime = riskless_algo()
    returnlist = []
    for mar1 in markets:
        m = 0
        returnstring = 'Market ID: '+str(debuglist[m][0])+', Market Name: '+ str(debuglist[m][1])+', Expected Profit per Share: '+ str(debuglist[m][2])+', Link to Market: https://www.predictit.org/markets/detail/'+str(debuglist[m][0])+' , Prices of Contracts: ' + str(debuglist[m][3])
        returnlist.append([returnstring])
        m = m+1
    return returnlist

# In[55]:




# In[ ]:





# In[ ]:





# In[ ]:




