#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint 

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

board


# In[ ]:




