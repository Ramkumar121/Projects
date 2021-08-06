#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import keyword
import operator
from datetime import datetime
import os


# In[2]:


print(keyword.kwlist) #


# In[3]:


len(keyword.kwlist) 


# In[4]:


val2 = 10


# In[5]:


print('val2')


# In[6]:


P1=10+20


# In[7]:


P1


# In[11]:


p=10
if p==10:
 print("value of p is 10 here")


# In[12]:


for i in range(0,5):
    print (i)


# In[13]:


j=20;
for i in range(0,5):
    print (i)
print (j)


# In[14]:


def square(num):
    '''square function will return the square of a given number'''
    return num**2;


# In[15]:


square(4)


# In[17]:


def evenodd(num):
    if num %2 == 0 :
        print ('given number is even')
    else:
        print ('given number is odd')


# In[18]:


evenodd(9)


# In[19]:


evenodd(8)


# In[21]:


str="helloworld"
print(len(str))


# str1='happy everyone'
# print(str1)

# In[22]:


str1='happy everyone'
print(str1)


# In[31]:


print(len(str1)) ### ## Calculate the length of the string"


# In[24]:


print(str1[5])


# In[25]:


str1[5] ## Fetch the fifth postion of the index for the string "happy everyone"


# In[26]:


str1[0:8] ### Fetch forward indexing postio 0 to  8 


# In[27]:


str1[-7] ### Fetch backward indexing postio -7 


# In[28]:


str1[-3:]  ### Fetch backward indexing postio -7 


# In[29]:


str1[5:] ### fetch the characters post indexing 5


# In[30]:


str1[0:4] ### fetch the first five character through forward indexing


# In[37]:


str1="ram"
str2="kumar"
a=str1+ "  "+str2 ### concat the given two strings 
print(a)


# str1="hello everyone"
#  for i in str1
#   print(i)

# In[38]:


str1="hello everyone" ### iterating the string
for i in str1:
    print(i)


# In[41]:


str1="hello everyone" ### iterating the string
for i in enumerate(str1):
    print(i)


# In[40]:


str1="hello everyone" ### iterating the string
for i in list(enumerate(str1)):
    print(i)


# In[42]:


string ="  Very good morning  "


# In[43]:


string.strip()


# In[44]:


string.rstrip()


# In[45]:


string.lstrip()


# In[46]:


string.lower()


# In[47]:


string.upper()


# In[48]:


string.replace("Very","Happy")


# In[49]:


string2="one two three one five one two three one two five four"


# In[51]:


string2.count("one")


# In[52]:


string2.count("three")


# In[53]:


string2.count("two")


# In[54]:


string2.replace(" ","")


# In[55]:


string3="Today is going to be a great day and wishing you success"


# In[56]:


mylist=string3.split()


# In[57]:


print(mylist)


# In[ ]:




