#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('results.csv')
df.head(10)


# #### Firstly, let's see the trend in the stock price of 10 companies on May 11

# In[3]:


plt.figure(figsize=(15,5))
ax = sns.lineplot(x='hour',y='highest_price',data=df,hue='company_name')


# #### We can see the stock prices were quite stable without any significant spike. Let's take a closer look at each company

# In[4]:


for company in df['company_name'].unique():
    print('Company:',company)
    df_trend = df[df['company_name'] == company].loc[:,['hour','highest_price']]
    print(df_trend.set_index('hour').plot(kind='line'))
    plt.show()


# Stock price of all 10 companies increased on May 11, 2021 <br />
# ●	Beyond Meat (BYND) <br />
# ●	Datadog (DDOG) <br />
# ●	Facebook (FB) <br />
# ●	Netflix (NFLX) <br />
# ●	Okta (OKTA) <br />
# ●	Pinterest (PINS)<br />
# ●	Shopify (SHOP)  <br />
# ●	Snap (SNAP) <br />
# ●	Square (SQ) <br />
# ●	The Trade Desk (TTD)

# ### Opening vs Closing Price

# In[5]:


sns.set(style="whitegrid")

df9 = df[(df['hour'] == 9)]

fig = plt.figure(figsize=(15,5))

bar_company = sns.barplot(x="company_name", y="highest_price", data=df9)

bar_company.set(xlabel='Company', ylabel='Highest Price at first trading hour')

plt.show()


# In[6]:


sns.set(style="whitegrid")

df15 = df[(df['hour'] == 15)]

fig = plt.figure(figsize=(15,5))

bar_company = sns.barplot(x="company_name", y="highest_price", data=df15)

bar_company.set(xlabel='Company', ylabel='Highest Price at last trading hour')

plt.show()


# In[ ]:




