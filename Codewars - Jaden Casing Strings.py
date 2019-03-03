#!/usr/bin/env python
# coding: utf-8

# In[1]:


#see Jaden Smith's twitter 

def toJadenCase(string):
    # ...
    working = string
    worklist = working.split(" ")
    reslist = []
    for word in worklist:
        reslist.append(word[0].upper() + word[1:])
    result = " ".join(reslist)
    print(result)
    
toJadenCase("How can mirrors be real if our eyes aren't real")


# In[18]:


#codewars best practice
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())

toJadenCase("How can mirrors be real if our eyes aren't real")


# In[ ]:




