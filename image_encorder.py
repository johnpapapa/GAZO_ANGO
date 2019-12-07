"""
macOS HighSierra version:10.13.6 
Python3.7.0
openCV 4.0.0.21
opencv-contrib-python 4.1.2.30
numpy 1.17.4
Pillow 6.2.1
"""
import cv2
import random
import numpy as np
from PIL import Image
import sys
import os


def Encrypt(file):
    print("Encrypting...")
    
    #create share pattern
    p_l = np.array([[[0,1],[0,1]],\
                    [[0,1],[1,0]],\
                    [[0,0],[1,1]],\
                    [[1,1],[0,0]],\
                    [[1,0],[0,1]],\
                    [[1,0],[1,0]]])

    img_l=[]
    for i in range(6,12):
        a = Image.open("Material-img/"+str(i)+".png","r")
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


    #Load secret image #please insert try to except
    #file = sys.argv
    secret = cv2.imread(file[1])
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

    
def Decrypt(file):
    print("Decrypting...")
    
    #Load share image
    share1 = cv2.imread(file[1])
    share2 = cv2.imread(file[2])

    #Check size & Create decrypt image 
    width1, height1, channel = share1.shape
    width2, height2, channel = share2.shape
    
    if(width1 == width2 and height1 == height2):
        secret = Image.new("RGB", (width1, height1), (255,255,255))
    else:
        print("Ignore image size")

    #Make Decrypt image
    for x in range(width1):
        for y in range(height1):
            px1 = share1[y, x]
            px2 = share2[y, x]
            
            if((px1 == [255,255,255]).all() and (px2 == [255,255,255]).all()):
                secret.putpixel((x, y), (255,255,255))
            else:
                secret.putpixel((x, y), (0,0,0))

    secret = np.asarray(secret)

    cv2.imwrite("DecryptImage.png", secret)

    
if __name__=="__main__":

    #ifCase command line module
    if len(sys.argv) == 2:
        try:
            if(os.path.exists(sys.argv[1]) == False):
                print(sys.argv[1]+" is not exist.")
                sys.exit()
        except Exception as e:
            print(e)
            sys.exit()

        Encrypt(sys.argv)

    elif len(sys.argv) == 3:
        try:
            if(os.path.exists(sys.argv[1]) == False):
                print(sys.argv[1]+" is not exist.")
                sys.exit()
            if(os.path.exists(sys.argv[2]) == False):
                print(sys.argv[2]+" is not exist.")
                sys.exit()                
        except Exception as e:
            print(e)
            sys.exit()
                
        Decrypt(sys.argv)

    else:
        raise Exception("missing file")
