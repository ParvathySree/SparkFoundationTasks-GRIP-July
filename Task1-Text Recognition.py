#!/usr/bin/env python
# coding: utf-8

# In[36]:


# importing modules
import cv2
import pytesseract
from pytesseract import Output


# In[37]:


# reading the image containing the printed text convertig it to rgb
confThres = 70
image = cv2.imread("novel.JPG")
RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



# In[38]:


# to find the locations of each areas in the text(dislayed as a dictionary)
out = pytesseract.image_to_data(RGB, output_type=Output.DICT)
print(out)


# In[39]:


# looping over each individual text so that we can extract the bounding box coordinates from its result
length = len(out["text"])
for i in range(0,length):

    x = out["left"][i]
    y = out["top"][i]
    w = out["width"][i]
    h = out["height"][i]

    text=out["text"][i] #ocr text
    conf=int(out["conf"][i]) #confidence values

  
    # filtering text localizations less than threshold confidence
    if conf > confThres:
            
        # display the text 
        print(text)
        
        
        
        cv2.rectangle(image, (x, y),(x + w, y + h),(255, 0, 0)) # draw bounding box
        cv2.putText(image,text,(x, y-10 ),cv2.FONT_HERSHEY_PLAIN,1, (0, 0, 255), 1) # to put text along with bounding box


# In[ ]:



#display image with text and output
cv2.imshow("Image with text",RGB)
cv2.imshow("Output", image)
cv2.waitKey(0)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




