#!/usr/bin/env python
# coding: utf-8

# In[2]:


#takes a letter(s) and a list, finds list entries that match the letters

import re
regex = re.compile('[^a-zA-Z]')
#First parameter is the replacement, second parameter is your input string
#syntax: regex.sub('', 'ab3d*E')
#Out: 'abdE'


def autocomplete(input_, dictionary):
    #your code here
    word = regex.sub('', input_)
    returnlist = []
    if len(dictionary) > 0:
        for val in dictionary:
            if word == val[:len(word)]:
                returnlist.append(val)
        return returnlist
    else:
        return word
    
    
print(autocomplete("a", ['abnormal','arm-wrestling','absolute','airplane','airport']))


# In[ ]:




