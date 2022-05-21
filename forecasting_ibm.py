#!/usr/bin/env python
# coding: utf-8

# In[15]:


model_id='66aa8303-2d3f-44ca-9ee8-663377db94ad'


# In[16]:


get_ipython().system('pip install ibm_watson_machine_learning')


# In[17]:


from ibm_watson_machine_learning import APIClient
wml_credentials = {
    "apikey":"RlZo16UuC65AHHppgs1DGimx2Q0-Ip7SmKmP_5WppCJF" , 
    "url":"https://eu-gb.ml.cloud.ibm.com"
}
client = APIClient(wml_credentials)


# In[18]:


def guid_from_space_name(client,space_name):
    space=client.spaces.get_details()
    return(next(item for item in space['resources'] if item['entity']["name"]==space_name)['metadata']['id'])


# In[19]:


space_uid=guid_from_space_name(client,'sales')
print("Space UID="+space_uid)


# In[20]:


client.set.default_space(space_uid)


# In[21]:


client.repository.download("66aa8303-2d3f-44ca-9ee8-663377db94ad","my_model.tar.gz")


# In[ ]:




