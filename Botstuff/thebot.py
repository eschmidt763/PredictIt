#!/usr/bin/env python
# coding: utf-8

# In[24]:


import discord
import RisklessAnalysis as ra
import asyncio


# In[25]:


token = 'NjQxMTAyNTgzODY3NjM3ODAw.XkNi_g.X7NnAfncw3f02c-Mc1EtwR6Mdtw'
client = discord.Client()


# In[26]:


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'Analyze now':
        response = ra.riskless_internal()
        await message.channel.send(response)


# In[27]:


client.run(token)


# In[ ]:




