#!/usr/bin/env python
# coding: utf-8

# In[6]:


n=int(input()) #enter the number of terms of the fibonacci series 
x=0
y=1
z=x+y
for i in range(0,n):
    z=x+y
    x=y
    y=z
    print((x),'', end='')


# In[ ]:




