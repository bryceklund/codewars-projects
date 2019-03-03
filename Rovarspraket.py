#!/usr/bin/env python
# coding: utf-8

# In[1]:


## take any word and append all consonants with an "o" and themselves
## eg. "b" becomes "bob", "r" becomes "ror", and "bread" becomes "bobroreadod"


# In[2]:


def rovarmaker(target):
    
    consonants = "bcdfghjklmnpqrstvxzwy"
    after_word = [""]
    count = 0

    for l in target:
        if l in consonants:
            after_word += l + "o" + l
        else:
            after_word += l
        count += 1
    final = "".join(after_word)
    return "'" + target + "'" + " translated is: " + final + "."
    

target = input("Give me a word to convert to Rövarspråket: ")
print(rovarmaker(target))


# In[ ]:




