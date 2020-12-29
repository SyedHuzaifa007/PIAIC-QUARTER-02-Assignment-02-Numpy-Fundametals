#!/usr/bin/env python
# coding: utf-8

# # Assignment For Numpy

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[1]:


import numpy as np
arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print("THIS IS THE ARRAY 1D AFTER CONVERION INTO 2D ARRAY WITH TWO ROWS:")
# print("=================================================================")
print(arr1.reshape(2,5))


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1]])
# In[18]:


a = np.arange(0,10).reshape(2,5)
b = np.ones((2,5),dtype=int).reshape(2,5)
# print("THIS IS THE OUTPUT AFTER STACKING THE TWO ARRAYS VERTICALLY:")
# print("=============================================================")
print(np.vstack((a,b)))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
# array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       # [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[19]:


a = np.arange(0,10).reshape(2,5)
b = np.ones((2,5),dtype=int).reshape(2,5)
# print("THIS IS THE OUTPUT AFTER STACKING THE TWO ARRAYS HORIZONTALLY:")
# print("=============================================================")
print(np.hstack((a,b)))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[36]:


a = np.array([0,1,2,3,4,5,6,7,8,9,]).reshape(5,2)
# print("THIS IS THE 1D ARRAY AFTER FLATTENING THE ARRAY OF SHAPE '5,2':")
# print("===============================================================")
print(np.ravel(a))


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
# array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[51]:


a = np.arange(0,15).reshape(5,3)
# print("THIS IS THE HIGHER DIMENSION ARRAY AFTER CONVERSION INTO 1D:")
# print("============================================================")
print(a.ravel())


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
# array([[ 0, 1, 2],
# [ 3, 4, 5],
# [ 6, 7, 8],
# [ 9, 10, 11],
# [12, 13, 14]])
# In[2]:


a = np.arange(0,15)
# print("THIS IS THE 1D ARRAY AFTER CONVERSION INTO HIGHER DIMENSION:")
# print("============================================================")
print(a.ravel())


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[3]:


a = np.arange(2,27).reshape(5,5)
# print("THIS IS THE ARRAY CONTAINING THE SQUARES OF THE ELEMENTS OF ARRAY 'a':")
# print("======================================================================")
print(np.square(a))

# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[70]:


a = np.random.randn(5,6)
# print("THIS IS THE MEAN OF THE ARRAY 'a':")
# print("==================================")
print(a.mean())


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[71]:


# print("THIS IS THE STANDARD DEVIATION OF THE ARRAY 'a':")
# print("================================================")
print(a.std())


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[72]:


# print("THIS IS THE MEDIAN OF THE ARRAY 'a':")
# print("====================================")
print(np.median(a))


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[75]:


# print("THIS IS THE TRANSPOSE OF THE ARRAY 'a':")
# print("=======================================")
print(a.transpose())


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[78]:


b = np.random.randn(4,4)
# print("THIS IS THE SUM OF THE DIAGONAL ELEMENTS OF THE ARRAY 'b':")
# print("==========================================================")
print(b.diagonal())


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[83]:


# print("THIS IS DETERMINANT OF THE ARRAY 'b':")
# print("=========================================")
print(b.diagonal())


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[91]:


c = np.arange(100).reshape(20,5)
# print("THIS IS THE 5th PERCENTILE OF ARRAY 'c': ")
# print("=========================================")
print(np.percentile (c, 5, axis=None, out=None))


# In[92]:


c = np.arange(100).reshape(20,5)
# print("THIS IS THE 95th PERCENTILE OF ARRAY 'c': ")
# print("==========================================")
print(np.percentile (c, 95, axis=None, out=None))


# ## Question:15

# ### How to find if a given array has any null values?

# In[7]:


a = np.array([120,50,5,np.NaN,25,68,34,0,80,np.NaN])
# print("THIS IS THE ARRAY OBTAINED AFTER CHECKING FOR NULL VALUES. 'FALSE' INDICATES THE RIGHT VALUE WHILE 'TRUE' INDICATES THE 'null' VALUE:")
# print("=====================================================================================================================================")
print(np.isnan(a))


# In[ ]:




