#!/usr/bin/env python
# coding: utf-8

# ## Derived datasets
# 
# We've already gone through how to use DCARTE to get UKDRI CRT raw datasets. However, a central element in the process of knowledge discovery (aka data science) is the creation of features that fuse different data sources, transform a single data source using some logic, or aggregate datasets to a relevant frequency.
# 
# Let's create a step by step example that will make this point simpler to follow. 

# We start by importing dcarte and loading PIR Activity across the houses 

# In[1]:


import dcarte 
import pandas as pd 
import seaborn as sns 
activity = dcarte.load('Activity','raw')
activity.start_date.agg(['min','max','count'])


# We then inspect the DataFrame's info()

# In[2]:


activity.info()


# In this example, we wish to convert the raw activity data into a wide one-hot encoding tabular format that allows us to easily analyse the level of activity among households over time (e.g. every six hours every day or every week). One of the first things we should look at is the frequency of activity throughout the various locations in order to simplify the data by deleting or merging certain areas around the household. The best technique to find such targets is to use the pandas plotting capabilities.

# In[3]:


activity.location_name.value_counts().plot.barh()


# The first step is to eliminate unique locations only in a few houses and combine contextually similar locations. This will make it easier to generalise our findings across all homes.

# In[4]:


location_by_pid =  pd.crosstab(activity.location_name,activity.patient_id)
location_by_pid


# In[5]:


ax = sns.heatmap(location_by_pid>0,cbar=False)
ax.tick_params(left=False, bottom=False)
ax.set_xticklabels([]);


# A simple interpretation of the above plot can be to do the following cleaning tasks: 
# - filter the cellar and the conservatory, 
# - merge WC1 and bathroom1 
# - merge study and office
# - merge the lounge, dining room and living room
# - merge the corridor and hallway 
# 
# Let's see an example of how to do this using pandas 
# 

# In[6]:


mask = ~activity.location_name.isin(['cellar','conservatory'])
activity = activity[mask]
activity.location_name.unique()


# There are many ways to remap one value into another value in Python. However, in the process of transparency, interpretability and ease of change, I find the dictionary approach shown below to be the simplest to foolow and implement. 

# In[7]:


mapping = {
    'bedroom1':'bedroom', 
    'bathroom1':'bathroom', 
    'hallway':'hallway', 
    'lounge':'lounge', 
    'kitchen':'kitchen',
    'living room':'lounge', 
    'corridor1':'hallway', 
    'dining room':'lounge', 
    'WC1':'bathroom', 
    'study':'study',
    'office':'study'}
activity.location_name = activity.location_name.map(mapping)
activity.location_name.unique()


# Revisiting the plots we used before is a useful sanity check to validate that the changes we made we applied. 

# In[ ]:


activity.location_name.value_counts().plot.barh()


# In[ ]:


ax = sns.heatmap(pd.crosstab(activity.location_name,activity.patient_id)>0,cbar=False)
ax.tick_params(left=False, bottom=False)
ax.set_xticklabels([]);


# After cleaning the location_name we can select just columns of intrest by passing a list of columns names to the DataFrame. 

# In[ ]:


activity[['start_date','patient_id','location_name']]


# Now, let's say we decide to merge the study with the lounge location, all we need to run the entire process again and update the mapping dictionary.  

# In[ ]:


activity = dcarte.load('Activity','raw',since='2022-02-01',until='2022-02-20',reload=False)
mask = ~activity.location_name.isin(['cellar','conservatory'])
activity = activity[mask]
mapping = {
    'bedroom1':'bedroom', 
    'bathroom1':'bathroom', 
    'hallway':'hallway', 
    'lounge':'lounge', 
    'kitchen':'kitchen',
    'living room':'lounge', 
    'corridor1':'hallway', 
    'dining room':'lounge', 
    'WC1':'bathroom', 
    'study':'lounge',
    'office':'lounge'}
activity.location_name = activity.location_name.map(mapping)
activity.location_name.unique()


# In the end, we now have a single dataset in which the majority of households are similar and there are very few homes with missing locations.

# In[ ]:


df = pd.crosstab(activity.location_name,activity.patient_id)
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt 
fig, ax = plt.subplots(figsize=(10,3))
sns.heatmap(df,  norm=LogNorm(),ax=ax)
ax.tick_params(left=False, bottom=False)
ax.set_xticklabels([]);


# Converting this dataset to a wide one-hot encoding format where time and patient ids are the indexes and the different locations are the columns requires calling a pandas function called `pd.get_dummies`.

# In[ ]:


activity = activity.set_index(['patient_id','start_date']).location_name
activity = pd.get_dummies(activity)
activity


# It would be helpful to formalise this process so that it does not require us to run it each time. Formalising derived datasets is another aspect of dcarte that simplifies the collaborations on different parts of data processing. Dcarte comes armed with three samples derived datasets that can be available using a simple command. Running any of the three functions listed below will add a single domain to your dcarte library. These functions will automatically download needed datasets and create the different local datasets described internally.

# In[ ]:


from dcarte.derived import (create_base_datasets,
                            create_weekly_profile)
create_base_datasets()


# In[ ]:


create_weekly_profile()


# When you run dcarte.domains() for the final time, you will notice that you now have a greater number of domains under your control than before. In the following section, we will go over one of these recipes in detail and show you how to create an expansion of it on your own using the material you have gained so far in this tutorial.

# In[ ]:


dcarte.domains()


# In[ ]:


df = dcarte.load('Activity_Dailies','profile')
df


# In[ ]:




