#!/usr/bin/env python
# coding: utf-8

# In[8]:


import glob as gl
import pandas as pd
import numpy as np
import time
import dask
import math as math
import datetime as dt


# In[9]:


csvlist = gl.glob("*.csv")


# In[10]:


len(csvlist)


# In[11]:


def listshift(listofcsvs):
    newcsvlist = [listofcsvs[-1]] + listofcsvs[:-1]
    return newcsvlist


# In[12]:


csvlist2 = listshift(csvlist)


# In[13]:


csvtestlist = csvlist[0:50]
csvtestlist2 = csvlist2[0:50]


# In[14]:


from dask.distributed import Client, progress
client = Client(threads_per_worker=8, n_workers=1)
client


# In[15]:


def cointtest(stock1, stock2, lagnumber, optionals=0):
    csv1 = pd.read_csv(stock1)
    price1_list = csv1['contract_best_buy_yes_price'].to_numpy()
    price1 = price1_list[0:-lagnumber]
    csv2 = pd.read_csv(stock2)
    price2_list = csv2['contract_best_buy_yes_price'].to_numpy()
    avg_list = []
    m_list = []
    c_list = []
    ratiolistlist = []
    goodlist = []
    if len(price1_list) == len(price2_list):
        try:
            for x in np.arange(lagnumber):
                price2 = price2_list[x:(-lagnumber+x)]
                #print(price2)
                ratiolist = price1/price2
                avg = np.mean(ratiolist)
                x_axis = np.arange(len(ratiolist))/len(ratiolist)
                A = np.vstack([x_axis, np.ones(len(x_axis))]).T
                #print(avg)
                m, c = np.linalg.lstsq(A, ratiolist, rcond=None)[0]
                avg_list.append(avg)
                m_list.append(m)
                c_list.append(c)
                ratiolistlist.append(ratiolist)
                if m < 0.1 and m > -0.1:
                    goodlist.append([m, lagnumber])
                else:
                    None
        except:
            m_list.append(1)
    else:
        m_list.append(1)
    avg_slope = np.mean(m_list)
    del csv1
    del csv2
    if optionals == 1:
        liststuff1 = [stock1, stock2, goodlist, avg_slope, avg_list, m_list, c_list, ratiolistlist]
        return liststuff1
    else:
        del price1_list
        del price1
        del price2_list
        del avg_list
        del m_list
        del c_list
        del ratiolistlist
        liststuff2 = [stock1, stock2, goodlist, avg_slope]
        return liststuff2


# In[16]:


def large_coint_test(stocklist1, stocklist2, lagnumber):
    goodstocklist = []
    badstocklist = []
    allstocklist = []
    dask_coint = dask.delayed(cointtest)
    dask_tasks_list = []
    for stock1, stock2 in zip(stocklist1, stocklist2):
        if stock1 == stock2:
            printphrase = str(stock1) + " and "+str(stock2)+" are the same stock, cannot do calculations!"
            allstocklist.append([printphrase])
            badstocklist.append([printphrase])
        else:
            task = dask_coint(stock1, stock2, lagnumber)
            dask_tasks_list.append(task)
    dask_persist_list = dask.persist(*dask_tasks_list)
    computations = dask.compute(dask_persist_list)
    return computations           


# In[17]:


def tasktime(list1, list2, lagnumber):
    starttime = dt.datetime.now()
    taskfile = large_coint_test(list1, list2, lagnumber)
    endtime = dt.datetime.now()
    time_elapsed = (endtime-starttime)
    return taskfile, time_elapsed


# In[22]:


wow, timeer = tasktime(csvlist, csvlist2, 120)


# In[23]:


print(timeer)


# In[26]:


for x in np.arange(len(wow[0])):
    if wow[0][x][2] != []:
        print(wow[0][x][0], wow[0][x][1],wow[0][x][2][0])
    else:
        None


# In[21]:





# In[ ]:





# In[ ]:




