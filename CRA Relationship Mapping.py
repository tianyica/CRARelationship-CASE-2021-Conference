#!/usr/bin/env python
# coding: utf-8

# In[87]:


import pandas as pd
import numpy as np
import scipy.stats as stats
from datetime import datetime
from datetime import date
import csv


# In[116]:


test = pd.read_csv('./FY1419/TrusteeFY1419P10.csv')


# In[117]:


values={'Ceased Date':date.today()}


# In[118]:


test=test.rename(columns={"ï»¿BN/Registration Number": "BN/Registration Number"})


# In[119]:


print(test)


# In[120]:


test['Appointed Date'] =  pd.to_datetime(test['Appointed Date'],format='%m/%d/%Y %H:%M')


# In[121]:


test['Ceased Date'] =  pd.to_datetime(test['Ceased Date'],format='%m/%d/%Y %H:%M')


# In[122]:


test = test.fillna(value=values)


# In[123]:


test['FullName']= test['First Name']+' '+test['Last Name']


# In[124]:


print(test['FullName'])


# In[125]:


grouped_test=test.groupby('BN/Registration Number')


# In[126]:


resultdf= pd.DataFrame(columns = ["FullName","FullName","BN/Registration Number"])


# In[127]:


print(resultdf)


# In[128]:


grouped_test.groups


# In[ ]:


i=0
k=0
s=0

for name, group in grouped_test:
    i=i+1
    k=0
    s=len(group)
    tempgroup=group
    while s>1:
        for index, row in tempgroup.iterrows():
            if k==0:
                tempFull=row['FullName']
                tempStart=row['Appointed Date']
                tempEnd=row['Ceased Date']
                tempOrg=row['BN/Registration Number']
                k=k+1
            if k>0:
                if not (row['Appointed Date']>tempEnd and row['Ceased Date']<tempStart):
                    print(str(row['FullName'])+"!"+str(tempFull)+"!"+str(tempOrg))
        tempgroup=tempgroup.drop(tempgroup.index[0])
        k=0
        s=s-1
                    
                


# In[ ]:




