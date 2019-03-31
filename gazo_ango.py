#macOS HighSierra version:10.13.6 
#Python3.7.0、openCV 4.0.0.21、numpy 1.15.1、Pillow 5.4.1
import cv2
import random
import numpy as np
from PIL import Image

#create share pattern
p_l = np.array([[[0,1],[0,1]],\
                [[0,1],[1,0]],\
                [[0,0],[1,1]],\
                [[1,1],[0,0]],\
                [[1,0],[0,1]],\
                [[1,0],[1,0]]])

img_l=[]
for i in range(6,12):
    a = Image.open(str(i)+".png","r")
    img_l.append(a)
    
#Distinguish share pattern as B,W
patternW = []
patternB = []
for y,p_y in enumerate(p_l):
    for x,p_x in enumerate(p_l):
        pp = p_y * p_x
        pv = [x,y]
        if (np.sum(pp < 1) == 4):
            patternB.append(pv)
        else:
            patternW.append(pv)

#Load secret image 
secret = cv2.imread("secret.png")
width,height,channel = secret.shape

#Create share image
canvas1 = Image.new("RGB", (width*2,height*2),(255,255,255))
canvas2 = Image.new("RGB", (width*2,height*2),(255,255,255))

#Make share image
for x in range(width):
    for y in range(height):
        px = secret[y,x]
        if( (px == [255,255,255]).all()):
            p = patternW[random.randint(0,len(patternW)-1)]
            canvas1.paste(img_l[p[0]],(x*2,y*2))
            canvas2.paste(img_l[p[1]],(x*2,y*2))
        else:
            p = patternB[random.randint(0,len(patternB)-1)]
            canvas1.paste(img_l[p[0]],(x*2,y*2))
            canvas2.paste(img_l[p[1]],(x*2,y*2))            
canvas1 = np.asarray(canvas1)
canvas2 = np.asarray(canvas2)

#Save share image
cv2.imwrite("share1.png",canvas1)
cv2.imwrite("share2.png",canvas2)


