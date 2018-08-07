
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import os
print(os.getcwd())


# In[7]:


os.chdir('C:\\Users\\Vaibhav\\Desktop')


# In[8]:


print(os.getcwd())


# In[10]:


stats=pd.read_csv('DemographicsData.csv')


# In[11]:


stats=pd.read_csv('DemographicData.csv')


# In[12]:


stats


# In[14]:


stats.head()


# In[15]:


stats.head(2)


# In[16]:


stats.tail()


# In[17]:


len(stats)


# In[19]:


stats.columns


# In[20]:


len(stats.columns)


# In[22]:


len(stats)


# In[23]:


stats.info()


# In[25]:


stats.describe()


# In[29]:


stats.describe().transpose()#give T also for transpose


# In[30]:


stats.describe().T


# In[32]:


stats.colnames()


# In[33]:


stats.columns


# In[34]:


lst=stats.columns


# In[35]:


lst


# In[36]:


stats.columns=['a','b','c','d','e']


# In[37]:


stats.head()


# In[38]:


stats.columns=lst


# In[39]:


stats.head()


# In[42]:


stats.Country \ Name


# In[43]:


stats.[Country Name]


# In[44]:


stats.columns = (['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers','IncomeGroup'])


# In[45]:


stats


# In[48]:


stats.CountryName


# In[49]:


stats.CountryName[5]


# In[52]:


stats.ContryName[:]


# In[53]:


#sunsetting....
stats[1:5]


# In[54]:


stats[::-10]


# In[55]:


stats[:10]


# In[56]:


stats[::20]


# In[57]:


stats[158:185]


# In[58]:


stats


# In[59]:


#subsetting Columns

stats['CountryName']


# In[60]:


stats['CountryName'].tail()


# In[61]:


stats['CountryName','BirthRate']


# In[65]:


stats['CountryName','BirthRate'] #use like that stats[['BirthRate','CountryName']]


# In[67]:


lst = ['CountryName','BirthRate']


# In[68]:


lst


# In[69]:


stats[lst].head()


# In[73]:


stats['CountryName'].head()


# In[75]:


stats[['BirthRate','CountryName']].head()


# In[76]:


stats.CountryName


# In[78]:


stats.BirthRate.head()


# In[80]:


stats[4:8][['BirthRate','CountryName']]


# In[82]:


stats[['CountryName','BirthRate']][4:8]


# In[83]:


stats[4:8]


# In[84]:


df=stats[4:8]


# In[85]:


df


# In[86]:


type(df)


# In[87]:


df2 = stats[['CountryName','BirthRate']]


# In[90]:


df2[4:8]


# In[91]:


stats[['CountryName','BirthRate','InternetUsers']][4:8]


# In[92]:


result = stats.BirthRate * stats.InternetUsers


# In[93]:


result


# In[94]:


result.head()


# In[95]:


type(result)


# In[96]:


stats[3,4]


# In[97]:


stats.iat[3,4]


# In[98]:


stats.head()


# In[101]:


stats.iat[0,0]


# In[104]:


stats.at[2,'BirthRate']


# In[110]:


stats.at[3,'IncomeGroup']


# In[111]:


stats[::10]


# In[112]:


sub10=stats[::10]


# In[115]:


sub10.iat[10,2]


# In[116]:


sub10.iat[2,2]


# In[118]:


stats.head(3)


# In[120]:


sub10.iat[0,4]


# In[122]:


stats.iat[2,2]


# In[124]:


sub10.iat[10,0]
sub10.at[10,'CountryName']


# In[128]:


#filtering data frame


# In[129]:


filter1 = (stats.InternetUsers < 2)


# In[130]:


filter1


# In[131]:


stats[30:40]


# In[137]:


filter1 = (stats.InternetUsers < 2)


# In[138]:


filter1


# In[139]:


stats[filter1]


# In[140]:


filter2=stats.BirthRate>40


# In[141]:


filter2


# In[142]:


stats[filter2]


# In[144]:


stats[filter1 | filter2 ]  #stats[filter1 or filter2 ] not applicable


# In[146]:


stats[filter1 & filter2 ]


# In[150]:


stats[stats.CountryCode == 'IND']


# In[151]:


stats.IncomeGroup.unique() #gives categories like factor in R


# In[152]:


stats.BirthRate.hist()


# In[154]:


from pylab import*


# In[155]:


stats.BirthRate.hist()


# In[156]:


df


# In[157]:


df = stats.set_index('CountryCode')


# In[159]:


df


# In[161]:


df = reset_index('CountryCode')


# In[162]:


df.reset_index()

