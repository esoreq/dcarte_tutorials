#!/usr/bin/env python
# coding: utf-8

# ## Developing a recipe of your own 
# 
# Until now, we covered how to configure and use dcarte to download the raw datasets collected by the ukdri. We've also learned that dcarte has three derived domains to extend its capabilities by adding some cleaning logic over the raw data.
# 
# In the last tutorial, we will create a new domain and one new derived dataset.

# We start like always by loading some key libraries. 

# In[1]:


import dcarte 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np 


# This notebook deconstructs the motion dataset in the base domain. We will go over the different steps taken to create this dataset as an example that I hope you can take further in your research.

# In[2]:


dcarte.__version__


# Here is a print screen of the output of reloading the entire motion dataset to review the different parts that create this simple building block dataset.   
# **please don't run this during the tutorial as it will take around 60 min to reconstruct this dataset completely**
# ![](imgs/figure-06.png)

# After the initial download, we have an updated version of the different parent datasets needed to reconstruct the motion dataset.  
# And as a result, dcarte will load the dataset from the local store, which is very fast.

# In[3]:


motion = dcarte.load('motion', 'base')


# As you can see, the motion dataset uses various datasets, all updated to a recent version since we just reloaded them.  
# let's load the different elements using dcarte.

# In[4]:


activity = dcarte.load('activity', 'raw')
entryway = dcarte.load('entryway', 'base')
bed_occupancy = dcarte.load('bed_occupancy', 'base')


# In[5]:


bed_occupancy.head(10)


# In[6]:


entryway.head(10)


# In[7]:


activity.head(10)


# In[8]:


from dcarte.utils import localize_time
activity = localize_time(activity,['start_date'])
activity.head(10)


# In[ ]:


fact = ['patient_id','location_name', 'start_date']
motion = pd.concat([activity[fact],bed_occupancy[fact],entryway[fact]])


# In[ ]:


motion = motion.sort_values(['patient_id','start_date'])


# In[ ]:


mapping = {'bathroom1': 'Bathroom', 
               'WC1': 'Bathroom',
               'kitchen': 'Kitchen',
               'hallway': 'Hallway',
               'corridor1': 'Hallway',
               'dining room': 'Lounge',
               'living room': 'Lounge',
               'lounge': 'Lounge',
               'bedroom1': 'Bedroom',
               'front door': 'Front door',
               'back door': 'Back door'}   
motion.location_name = motion.location_name.map(mapping)


# In[ ]:


motion = motion[~motion.location_name.isin(['office', 
                                                'conservatory', 
                                                'study', 
                                                'cellar'])]   


# In[ ]:


motion.head(10)


# In[ ]:


motion = motion.reset_index(drop=True)


# In[ ]:


motion.head(10)


# In[ ]:


from dcarte.local import LocalDataset
from dcarte.config import get_config
cfg = get_config()


# In[ ]:


cfg


# In[ ]:


domain = 'base'
module = 'base'
parent_datasets = [['activity','raw'],
                   ['entryway','base'],
                   ['bed_occupancy','base']]
p_datasets = {d[0]:dcarte.load(*d) for d in parent_datasets}
_ = LocalDataset(dataset_name = 'motion_new',
             datasets = p_datasets,
             pipeline = ['process_motion'],
             domain = domain,
             module = module,
             module_path = f'{cfg["data_folder"]}/recipes/{domain}/{module}.py',
             dependencies = parent_datasets)


# In[ ]:


dcarte.domains()


# In[ ]:


dcarte.load('Homes','lookup')

