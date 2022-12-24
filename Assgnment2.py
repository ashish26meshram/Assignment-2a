#!/usr/bin/env python
# coding: utf-8

# In[38]:


def last(n):
    return n[-1]
x=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
y=[len(x)-1]
z= sorted(x, key=last)
print(z)


# In[ ]:




