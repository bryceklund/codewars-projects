#!/usr/bin/env python
# coding: utf-8

# In[1]:


#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

def square_digits(num):
    presq = [n for n in str(num)]
    postsq = [int(digit) ** 2 for digit in presq]
    resultstr = ""
    count = 0
    for val in postsq:
        resultstr += str(postsq[count])
        count += 1
    return int(resultstr)
    
square_digits(9119)


# In[ ]:




