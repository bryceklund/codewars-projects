#!/usr/bin/env python
# coding: utf-8

# In[8]:


#check whether there is an equal number of Xs and Os in a string
    
def xo(s):
    return s.lower().count("x") == s.lower().count("o")
    #return s.lower().count("o")
    
print(xo("hfxgOh"))


# In[ ]:




