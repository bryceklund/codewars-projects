#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#check if the input string is a pangram

import string
import re
def is_pangram(s):
    #''.join([i for i in s if i.isalpha()])
    #work = regex.sub('', ''.join(sorted(set(s.lower()))).replace(" ", ""))
    work = ''.join(sorted(set([i for i in s.lower() if i.isalpha()]))).replace(" ", "")
    if len(work) == len(string.ascii_lowercase):
        return True
    else:
        return False

is_pangram("the quick    #$$#%&%^*#$k brown     fox ju@$%^@$mps ov@$##er the l    azy dog!\][\]")


# In[2]:


#codewars best practice
import string

def is_pangram(s):
    print(set(string.ascii_lowercase)) 
    print(set(s.lower()))
    return set(string.ascii_lowercase) <= set(s.lower())

is_pangram("the qk    #$$#%&%^*#$k brown     fox ju@$%^@$mps ov@$##er the l    azy dog!\][\]")


# In[ ]:




