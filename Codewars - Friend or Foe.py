#!/usr/bin/env python
# coding: utf-8

# In[4]:


#i am only friends with people whose names are four letters long

def friend(x):
    #Code
    friends = []
    for name in x:
        if len(name) == 4:
            friends.append(name)
    return friends


print(friend(["Ryan", "Kieran", "Mark"]))


# In[ ]:




