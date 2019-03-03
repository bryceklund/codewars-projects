#!/usr/bin/env python
# coding: utf-8

# In[1]:


#how many times does d appear in n**2?

def nb_dig(n, d):
    # your code
    n = n
    klist = []
    kliststr = None
    ncount = 0
    for k in range(n + 1):
        squared = k ** 2
        klist.append(squared)
    kliststr = "".join(str(nums) for nums in klist)
    for num in kliststr:
        if num == str(d):
            ncount += 1
    return ncount

print(nb_dig(10, 1))


# In[41]:


#codewars best practice

def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))

print(nb_dig(10, 1))


# In[ ]:




