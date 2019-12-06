#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Analysis as an


# In[2]:


contractJ1sql = "'Joe Biden'"
contractJ2sql = "'Joe Biden'"
marketJ2sql = "'Who will win the 2020 Democratic presidential nomination?'"
marketJ1sql = "'Who will win the 2020 U.S. presidential election?'"
contractJ1 = 'Joe Biden'
contractJ2 = 'Joe Biden'
marketJ2 = 'Who will win the 2020 Democratic presidential nomination?'
marketJ1 = 'Who will win the 2020 U.S. presidential election?'
csvfilenow = 'BidenAnalysis.csv' 
csvhist = 'biden.csv'
buyaggros = 0.3
sellaggros = 0.3
zztop = 1
s1name = 'Joe Biden for President 2020'
s2name = 'Joe Biden for Democratic Nomination 2020'


# In[ ]:


an.analysis_loop(csvhist, csvfilenow, marketJ1sql, marketJ2sql,contractJ1sql, 
              contractJ2sql, marketJ1, marketJ2, contractJ1, contractJ2,
                buyaggros, sellaggros, zztop, s1name, s2name)


# In[4]:




