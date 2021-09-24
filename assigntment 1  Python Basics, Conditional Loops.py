#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line."""
n=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5 != 0):
        n.append(str(i))
        print (','.join(n))


# In[ ]:





# In[2]:


"""2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name."""
fname = input("Enter your first name ")
lname = input("Enter your last name ")
print(lname[::-1] + " " + fname[::-1])


# In[3]:


"""Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3
diameter = 2r
radius = diameter/2"""
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# In[ ]:





# In[ ]:




