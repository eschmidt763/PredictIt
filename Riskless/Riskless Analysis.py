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


def riskless_internal(debug_file):
    now= datetime.now()
    nowstring = now.hour
    webhook = Webhook.partial(674056380772253697, 
                             'RTuPvf30qDTtx-WM3s_bfiqxtEJ29KRHadOOqW-2glW-zfCW1Q8NHFIRu1px7qU2RqFi', 
                              adapter=RequestsWebhookAdapter())
    previouslist = []
    prev_ids = []
    while nowstring != 3:
        marketlist, debuglist, ids, runtime = riskless_algo()
#        print(marketlist)
#        print(debuglist)
#        print(ids)
        if debuglist == []:
            if previouslist != []:
                webhook.send('Markets are no longer riskless!')
            else:
                None
        else:
            n = 0
            m = 0
            for prev_id in prev_ids:
                n = n+1
                if prev_ids == []:
                    None
                elif prev_id not in ids:
                    webhook.send('Market no longer riskless! Market ID: '+str(prev_id)+', Market Name: '+
                     previouslist[n-1][1])
                else:
                    None
            for good_id in ids:
                m = m+1
                if good_id in prev_ids:
                    None
                else:
                    webhook.send('Market ID: '+str(good_id)+', Market Name: '+
                     debuglist[m-1][1]+', Expected Profit per Share: '+ str(debuglist[m-1][2])
                    +', Link to Market: https://www.predictit.org/markets/detail/'+str(good_id)+
                                 ' , Prices of Contracts: ' + str(debuglist[m-1][3]))
        previouslist = debuglist
        prev_ids = ids
        with open(debug_file, 'a') as file:
            writer = csv.writer(file)
            line = debuglist
            insertion = ([datetime.now()]+line)
            writer.writerow(insertion)
        file.close()
        time.sleep(60)
        now= datetime.now()
        nowstring = now.hour
    else:
        time.sleep(60)
        now= datetime.now()
        nowstring = now.hour
        riskless_internal(debug_file)


# In[55]:


def riskless_loop():
    debug_file = 'riskless_debug_file.csv'
    if os.path.exists(debug_file) == True:
        os.remove(debug_file)
        try: 
            riskless_internal(debug_file)
        except: 
            time.sleep(60)
            riskless_loop()
    else:
        try:
            riskless_internal(debug_file)
        except:
            time.sleep(60)
            riskless_loop()


# In[56]:


riskless_loop()


# In[ ]:





# In[ ]:





# In[ ]:




