#!/usr/bin/env python
# coding: utf-8

# In[1]:


import AnalysisMaker as am
import database_functions as db
import Notification as nt
import datetime as dt
import os
import time
import numpy as np
import pandas as pd


# In[19]:


def analysis_loop(csvhistfile, csvfilecurrent, market1sql, market2sql, contract1sql, contract2sql,
                  market1, market2, contract1, contract2,
                 buyaggro, sellaggro, zscore, stock1name, stock2name):
    if os.path.exists(csvfilecurrent) == True:
        sendmessage = [[0]]
        file_ext_time = dt.datetime.now()
        file_ext_month = file_ext_time.month
        file_ext_day = file_ext_time.day
        text_file_name = "debug-text-"+contract1+str(file_ext_month)+'-'+str(file_ext_day)+".txt"
        nums_file_name = "debug-nums-"+contract1+str(file_ext_month)+'-'+str(file_ext_day)+".txt"
        am.csvcreator(csvfilecurrent, market1sql, market2sql, contract1sql, contract2sql)
        #am.hist_and_current_db(csvhistfile, csvfilecurrent)
        now= dt.datetime.now()
        nowstring = now.hour
        while nowstring != 3:
            try:
                am.csv_appender_func(csvfilecurrent, market1, market2, contract1, contract2)
                debugs = nt.notifyMe(csvfilecurrent, buyaggro, sellaggro, zscore, stock1name, stock2name, sendmessage[-1])
                debugger_text_file = open(text_file_name, "a")
                #df = pd.read_csv(csvfilecurrent)
                #numpy_df = np.asarray(df)
                #s1 = numpy_df[:,1]
                #s2 = numpy_df[:,2]
                #debug = nt.pairsTradeNotificationFunction(s1, s2, buyaggro, sellaggro, zscore, stock1name, stock2name)
                #print(debug)
                textstring = str(debugs[1]) + ', ' + str(debugs[3])+ ' \n'
                debugger_text_file.write(textstring)
                debugger_text_file.close()
                debugger_nums_file = open(nums_file_name, "a")
                numstring = str(debugs[2])+' \n'
                debugger_nums_file.write(numstring)
                debugger_nums_file.close()
                sendmessage.append(debugs[0])
                time.sleep(60)
                now= dt.datetime.now()
                nowstring = now.hour
            except:
                time.sleep(60)
                now= dt.datetime.now()
                nowstring = now.hour 
        else:
            time.sleep(120)
            now= dt.datetime.now()
            nowstring = now.hour
            analysis_loop(csvhistfile, csvfilecurrent, market1sql, market2sql, contract1sql, contract2sql,
                  market1, market2, contract1, contract2,
                 buyaggro, sellaggro, zscore, stock1name, stock2name)
    else:
        sendmessage = [[0]]
        file_ext_time = dt.datetime.now()
        file_ext_month = file_ext_time.month
        file_ext_day = file_ext_time.day
        text_file_name = "debug-text-"+contract1+str(file_ext_month)+'-'+str(file_ext_day)+".txt"
        nums_file_name = "debug-nums-"+contract1+str(file_ext_month)+'-'+str(file_ext_day)+".txt"
        am.csvcreator(csvfilecurrent, market1sql, market2sql, contract1sql, contract2sql)
        #am.hist_and_current_db(csvhistfile, csvfilecurrent)
        now= dt.datetime.now()
        nowstring = now.hour
        while nowstring != 3:
            try:
                am.csv_appender_func(csvfilecurrent, market1, market2, contract1, contract2)
                debugs = nt.notifyMe(csvfilecurrent, buyaggro, sellaggro, zscore, stock1name, stock2name, sendmessage[-1])
                debugger_text_file = open(text_file_name, "a")
                #df = pd.read_csv(csvfilecurrent)
                #numpy_df = np.asarray(df)
                #s1 = numpy_df[:,1]
                #s2 = numpy_df[:,2]
                #debug = nt.pairsTradeNotificationFunction(s1, s2, buyaggro, sellaggro, zscore, stock1name, stock2name)
                #print(debug)
                textstring = str(debugs[1]) + ', ' + str(debugs[3])+ ' \n'
                debugger_text_file.write(textstring)
                debugger_text_file.close()
                debugger_nums_file = open(nums_file_name, "a")
                numstring = str(debugs[2])+' \n'
                debugger_nums_file.write(numstring)
                debugger_nums_file.close()
                sendmessage.append(debugs[0])
                time.sleep(60)
                now= dt.datetime.now()
                nowstring = now.hour
            except:
                time.sleep(60)
                now= dt.datetime.now()
                nowstring = now.hour 
        else:
            time.sleep(120)
            now= dt.datetime.now()
            nowstring = now.hour
            (csvhistfile, csvfilecurrent, market1sql, market2sql, contract1sql, contract2sql,
                  market1, market2, contract1, contract2,
                 buyaggro, sellaggro, zscore, stock1name, stock2name)       
    return
                    
        

