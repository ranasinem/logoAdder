import cv2
import glob 
import numpy as np 

def overlay(img1,img2):
    h, w, c = img2.shape
    img1 = cv2.resize(img1, (w, h), interpolation = cv2.INTER_CUBIC)
    result = np.zeros((h, w, 3), np.uint8)
    alpha = img2[:, :, 3] / 255.0
    result[:, :, 0] = (1. - alpha) * img1[:, :, 0] + alpha * img2[:, :, 0]
    result[:, :, 1] = (1. - alpha) * img1[:, :, 1] + alpha * img2[:, :, 1]
    result[:, :, 2] = (1. - alpha) * img1[:, :, 2] + alpha * img2[:, :, 2]
    return result

path='input/*.*'
img_number = 1

for file in glob.glob(path):  #ıterate through each file
    a=cv2.imread(file) #read each file
    b=cv2.imread('logo.png',-1)
    out=overlay(a,b)
 
    cv2.imwrite('output/output'+str(img_number)+'.jpg',out)
    img_number+=1
