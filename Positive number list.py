#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Python Program to print Positive Number in a List

def positive_number(NumList):
    for j in range(Number):
        if(NumList[j] >= 0):
            print(NumList[j],end=' ')
            
NumList=[]
Number = int(input("Please Enter the Total Number of List Element:"))
for i in range(1,Number+1):
    value = int(input("Please enter the value of %d Element:" %i))
    NumList.append(value)
    
print("\nPositive Number in thisList are;")
positive_number(NumList)


# In[ ]:





# In[ ]:




