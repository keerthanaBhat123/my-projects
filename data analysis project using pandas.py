#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


df=pd.read_csv(r"C:\Users\Keerthana N Bhat\Downloads\file.csv")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[6]:


df.shape


# In[8]:


df.columns


# In[9]:


df.dtypes


# In[12]:


df.info()


# # duplicate
# 

# In[13]:


df.head()


# In[15]:


df.shape


# In[17]:


df[df.duplicated()]


# In[20]:


df.drop_duplicates(inplace=True)


# In[21]:


df[df.duplicated()]


# In[22]:


df.shape


# # finding null value.if find any null value it should be showed with heat map

# In[8]:


df.isnull()


# In[25]:


df.isnull().sum()


# # seaborn library (heat-map)

# In[12]:


import seaborn as sns


# In[29]:


sns.heatmap(df.isnull())


# # for house of cart ,what is the show id and who is the director

# In[ ]:


isin()


# In[30]:


df.head()


# In[35]:


df[df['Title'].isin(['House of Cards'])]


# In[38]:


df[df['Title'].str.contains('House of Cards')]


# # 2. in what year highest no of tv shows and movies were released

# In[39]:


df.dtypes


# In[40]:


df['date_N']=pd.to_datetime(df['Release_Date'])


# In[42]:


df.head()


# In[57]:


df['Title'].iloc[3]


# In[58]:


df.dtypes


# In[60]:


df['date_N'].dt.year.value_counts()


# # Bar graph

# In[61]:


df['date_N'].dt.year.value_counts().plot(kind='bar')


# # 3.How many movies and tv are in the database? show with bar graph

# In[67]:


df.head(2)


# In[69]:


df.groupby('Category').Category.count()


# In[77]:


df['Category'].value_counts().plot(kind='bar')


# # 4.show all the movies that were released in 2000

# In[78]:


df.head(2)


# In[85]:


df['year']=df['date_N'].dt.year


# In[86]:


df.head(2)


# In[87]:


#filtering


# In[88]:


df[(df['Category']=='Movie') & (df['Year']==2020)]


# # 5.show only the title of all TV shows that were released only in india
# 

# In[90]:


df[(df['Category']=='TV Show') & (df['Country']=='India')] ['Title']


# # 6.Top 10 director who gave highest no of TV shows & movies to netflix

# In[91]:


df.head(2)


# In[10]:


df_director=df['Director'].value_counts().head(10)
df_direct


# # 7.Show all the records where category is movie and type is comedies or country is united kingdom

# In[99]:


df.head(2)


# In[105]:


df[(df['Category']=='Movie')& (df['Type']=='Comedies')| (df['Country']=='United Kingdom')]


# # 8. How many Movies got the tv-14 rating in canada

# In[106]:


df.head(2)


# In[126]:


df[(df['Category']=='TV Show') & (df['Rating'] =='TV-14')]


# 

# In[127]:


df[(df['Category']=='TV Show') & (df['Rating'] =='TV-14')].shape


# In[128]:


df[(df['Category']=='TV Show') & (df['Rating'] =='TV-14')&(df['Country']=='Canada')]


# In[129]:


df[(df['Category']=='TV Show') & (df['Rating'] =='TV-14')&(df['Country']=='Canada')]


# # 9 how many tv shows got R rating after 2018

# In[130]:


df.head(2)


# In[135]:


df[(df['Category']=='TV Show') & (df['Rating'] =='R')& (df['Year']>2018)]


# # 10. what is the maximum duration of a movie/show on netflix

# In[136]:


df.head(2)


# In[151]:


df.Duration.unique()


# # which individual country has highest no of tv show

# In[152]:


df.head()


# In[159]:


df_tv_shows=df[df['Category']=='TV Show']
df_tv_shows


# In[160]:


df_tv_shows.Country.value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




