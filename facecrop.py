import cv2
import glob
import numpy as np
import json
import os
#import sys

#cascade file
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
images = []
image_name=[]

bbox_master=[]

#################----PATH---############################
path='C:/Users/Naman Pundir/Documents/CSE700/data'
#print(path)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
#Reading of images
for img in glob.glob(path+"/*.jpg"):
    
  n= cv2.imread(img)
  #n=n-10 #changing intensity for better matches?
  faces = face_cascade.detectMultiScale(n, 1.2, 5)
   
  img_name = os.path.basename(img).split('.')[0]
  bbox_per_image = dict()
  count=0
# Draw rectangle around the faces and crop the faces
  for (x, y, w, h) in faces:
	  cv2.rectangle(n, (x, y), (x+w, y+h), (0, 0, 255), 2)
	  bboxxx = (y,y + h, x,x + w)
	  face = n[y:y + h, x:x + w]
	  #bbox dictionary to store faces and bbo
	  bbox_per_image[img_name+'_'+str(count)+'.jpg'] = str(bboxxx)
	  #cv2.imshow("face",faces)#############################################################redo: img (1)_0.jpg, img (2)_0.jpg
	  cv2.imwrite('C:/Users/Naman Pundir/Documents/CSE700/face1/'+img_name+'_'+str(count)+'.jpg',face); ###to save each face with imagename in front
	  count = count + 1
  bbox_master.append(bbox_per_image)
with open('bbox_master.json', 'w') as outfile:
    json.dump(bbox_master, outfile)
# Display the output
#cv2.imwrite('detcted.jpg', img)
#cv2.imshow('img',img)
    #cv2.waitKey()