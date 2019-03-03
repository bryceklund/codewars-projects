#!/usr/bin/env python
# coding: utf-8

# In[19]:


# my initial code
def generateShape(int):
    for x in range(int):
        "+" * int
        
print(generateShape(5))


# In[13]:


# my revision
def generateShape(n):
    return ((("+" * n) + "\n") * n)


# In[2]:


# working version of my revision
def generateShape(n):
    return ((("+" * n) + "\n") * n)[:-1]


print(generateShape(5))


# In[ ]:




