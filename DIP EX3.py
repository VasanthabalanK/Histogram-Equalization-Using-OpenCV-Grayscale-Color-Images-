#!/usr/bin/env python
# coding: utf-8

# ### EXP-3 Histogram Equalization
# ### NAME:VASANTHABALAN K
# ### REG.NO:212224230296

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


img = cv2.imread('images (1).jpg', cv2.IMREAD_GRAYSCALE)


# In[3]:


plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.show()


# In[4]:


plt.hist(img.ravel(),256,range = [0, 256]);
plt.title('Original Image')
plt.show()


# In[5]:


img_eq = cv2.equalizeHist(img)


# In[6]:


plt.hist(img_eq.ravel(), 256, range = [0, 256])
plt.title('Equalized Histogram')


# In[9]:


plt.imshow(img_eq, cmap='gray')
plt.title('Original Image')
plt.show()


# In[10]:


img = cv2.imread('images (1).jpg', cv2.IMREAD_COLOR)


# In[11]:


img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# In[12]:


img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:, :, 2])


# In[13]:


img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)


# In[14]:


plt.imshow(img_eq[:,:,::-1]); plt.title('Equalized Image');plt.show()


# In[15]:


plt.hist(img_eq.ravel(),256,range = [0, 256]); plt.title('Histogram Equalized');plt.show()


# In[16]:


plt.figure(figsize = (20,10))
plt.subplot(221); plt.imshow(img[:, :, ::-1]); plt.title('Original Color Image')
plt.subplot(222); plt.imshow(img_eq[:, :, ::-1]); plt.title('Equalized Image')
plt.show()


# In[17]:


plt.figure(figsize = [15,4])
plt.subplot(121); plt.hist(img.ravel(),256,range = [0, 256]); plt.title('Original Image')
plt.subplot(122); plt.hist(img_eq.ravel(),256,range = [0, 256]); plt.title('Histogram Equalized')


# In[ ]:




