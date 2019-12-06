#!/usr/bin/env python
# coding: utf-8

# In[19]:


import sqlalchemy as db
import pandas as pd
import numpy as np
import database_functions as dat
import csv
import dbconn

from dbconn import CONN


# In[33]:


def csvcreator(csvname, market1, market2, contract1, contract2):
    engine1 = db.create_engine('CONN')
    engine2 = db.create_engine('CONN')
    str_sql1 = db.sql.text("SELECT contract_best_buy_yes_price from contracts where market_name like " + market1 + " and contract_name like "+ contract1 + " ORDER BY contracts.date desc limit 20000")
    str_sql2 = db.sql.text("SELECT contract_best_buy_yes_price from contracts where market_name like " + market2 + " and contract_name like "+ contract2 + " ORDER BY contracts.date desc limit 20000")
    #str_sql1 = db.sql.text("SELECT contract_best_buy_yes_price from contracts where market_name like " + market1 + " and contract_name like "+ contract1)
    #str_sql2 = db.sql.text("SELECT contract_best_buy_yes_price from contracts where market_name like " + market2 + " and contract_name like "+ contract2)
    results1 = engine1.execute(str_sql1).fetchall()
    results2 = engine2.execute(str_sql2).fetchall()
    indexy = np.arange(len(results1))
    np.savetxt(csvname, np.column_stack((indexy, results1, results2)), delimiter=",", fmt='%s')
    return
    
    
def hist_and_current_db(histcsv, currentcsv):
    sourcefilehist = open(histcsv, 'r')
    data1 = sourcefilehist.read()
    with open(currentcsv, 'a') as destFile:
        destFile.write(data1)
    
    return
    
def csv_appender_func(whole_csv, market1, market2, contract1, contract2):
    with open(whole_csv, 'a') as file:
        writer = csv.writer(file)
        line = dat.pricecsvmaker(market1, market2, contract1, contract2)
        insertion = ([0]+line)
        writer.writerow(insertion)
    return


# In[34]:





# In[35]:





# In[23]:





# In[ ]:




