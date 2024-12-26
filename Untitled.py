#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[142]:


data = pd.read_csv(os.getcwd() + '\\data\\Dataset for gbm\\Train.csv', encoding = "ANSI")
print(data.dtypes)
print('\nSize:', data.shape)


# In[143]:


#count unique values in a column
data.groupby(by = 'City').nunique()


# In[144]:


#unique value in entire data frame
data.nunique(axis=0)


# In[145]:


#Target vatiable 
data['Disbursed'].value_counts()


# In[146]:


#missing values
data.isnull().sum().sort_values(ascending=False)


# In[147]:


data.drop(columns=['City', 'LoggedIn', 'Salary_Account', 'Employer_Name', 'Lead_Creation_Date'], inplace=True)


# In[148]:


now = pd.Timestamp('now')
data['DOB'] =  pd.to_datetime(data['DOB'])
data['DOB'] = data['DOB'].where(data['DOB'] < now, data['DOB'] -  np.timedelta64(100, 'Y'))
data['Age'] = (now - data['DOB']).astype('<m8[Y]')
data.drop(columns='DOB', inplace=True)


# In[199]:


from sklearn.impute import SimpleImputer
impute = SimpleImputer(missing_values=np.nan, strategy='median')
imputed = impute.fit(np.array(data['Existing_EMI']).reshape(-1,1))
data['Existing_EMI'] = imputed.transform(np.array(data['Existing_EMI']).reshape(-1,1))

imputed2 = impute.fit(np.array(data[['Loan_Tenure_Applied', 'Loan_Amount_Applied']]).reshape(-1, 2))
data[['Loan_Tenure_Applied', 'Loan_Amount_Applied']] = imputed2.transform(np.array(data[['Loan_Tenure_Applied', 'Loan_Amount_Applied']]).reshape(-1,2))


# In[195]:


3,6,9,10,12


# In[200]:


get_ipython().run_line_magic('lsmagic', '')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[27]:


mongo = pd.read_json("E:\\mongo_all_types.json")
mongo.drop(['double_', 'int32_', 'undefined_', 'nan_'], axis=1, inplace=True)
mongo4= mongo.loc[4,:]
mongo4


# In[44]:


from pandas.io.json import json_normalize
mongodf = pd.concat([pd.DataFrame(mongo), json_normalize(mongo4['obj_A'])], axis=1)
mongodf


# In[39]:


json_normalize(mongo4['obj_A'])


# In[41]:


pd.DataFrame(mongo)


# In[ ]:




