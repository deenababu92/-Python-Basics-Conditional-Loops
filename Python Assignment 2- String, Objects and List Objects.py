#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.Create the below pattern using nested for loop in Python.

"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""


# In[2]:


n = int(input("enter the number"))

for i in range(n):
    for j in range(i):
        print(" *",end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print(" *",end="")
    print('')


# In[3]:


#Nested 
#n = int(input("enter the number"))

n = 6
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

# Start the loop to print the remaining rows in decreasing order of stars
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# # 2. Write a Python program to reverse a word after accepting the input from the user.
# 
# Input word: ineuron
# Output: norueni

# In[11]:


n = input("Enter your word ")
for i in range(len(n) - 1, -1, -1):
    print(n[i], end="")
print("\n")


# In[22]:


n = input("Enter your word ")
n[::-1]


# In[ ]:





# In[ ]:




