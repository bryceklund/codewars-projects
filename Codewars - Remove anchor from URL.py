#!/usr/bin/env python
# coding: utf-8

# In[2]:


def remove_url_anchor(url):
    # TODO: complete
    worklist = [letter for letter in url]
    if '#' in worklist:
        del worklist[worklist.index('#'):]
        return ''.join(worklist)
    else:
        return ''.join(worklist)

remove_url_anchor('www.codewars.com#about')


# In[16]:


#best practice
def remove_url_anchor(url):
    return url.split('#')[0] #splits the string into a list on the specified value (is present). selects the index to return, in this case, the first one.

remove_url_anchor('www.codewars.com#bout')


# In[ ]:




