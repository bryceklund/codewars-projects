#!/usr/bin/env python
# coding: utf-8

# In[49]:


#creates a sequence n integers long with the formula n = n + (previous two digits)

def tribonacci(signature, n):
    
    sequence = signature[:]
    count = 4
    currentindex = 3
    result = 0

    while count <= n and n != 0:
        result = sum(sequence[currentindex-3:currentindex])
        sequence.append(result)
        count += 1
        currentindex += 1
    
    if n == 0:
        return []
    else:
        return sequence[:n]
    
    
    
tribonacci([1, 1, 1], 10)


# In[55]:


#best practice from codewars

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    print(len(signature))
    return res

tribonacci([1, 1, 1], 10)


# In[ ]:




