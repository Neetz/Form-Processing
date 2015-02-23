import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from PIL import Image
import os

def load(img1,img2):
    img1 = cv2.imread(img1,0)
    img2 = cv2.imread(img2,0)
    return img1,img2

def preprocess(img):
    blur = cv2.GaussianBlur(img,(9,9),0)
    ret1,th = cv2.threshold(blur,0,255,cv2.THRESH_OTSU)
    median = cv2.medianBlur(th,5)
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.erode(median,kernel,iterations = 1)
    return dilation

def substract_images(img1,img2):

    img3=img1-img2
    res = ndimage.binary_opening(img3)
    plt.imsave("../meta-data/pre-result1.jpg",res)

def crop_image(img,left,top,right,bottom):
    cropped_image = img.crop((left, top, right, bottom))
    return cropped_image

def get_name(test_image):
    img = Image.open(test_image)
    width, height = img.size   # Get dimensions
    left = width/6
    top = 4*height/26
    right = 11 * width/20
    bottom = (19*height)/100
    name=crop_image(img,left,top,right,bottom)
    name.save("../meta-data/name.jpg",quality=100,grayscale=True)

def get_usn(test_image):
    img = Image.open(test_image)
    width, height = img.size   # Get dimensions
    left = 19*width/100
    top = 5*height/26
    right = 2 * width/5
    bottom = 11*height/50
    name=crop_image(img,left,top,right,bottom)
    name.save("../meta-data/usn.jpg",quality=100)

def get_branch(test_image):
    img = Image.open(test_image)
    width, height = img.size   # Get dimensions
    left = 31*width/50
    top = 5*height/26
    right = 18*width/25
    bottom = 11*height/51
    name=crop_image(img,left,top,right,bottom)
    name.save("../meta-data/branch.jpg",quality=100)

def extract_fields(image):
    get_name(image)
    get_usn(image)
    get_branch(image)

def cleanup():
    os.rmdir("../meta-data")

def setup():
    os.mkdir("../meta-data")

if __name__ == "__main__":
    setup()
    img1,img2=load("../source/original_form2.jpg","../source/filled2.jpg")
    clean_img1=preprocess(img1)
    clean_img2=preprocess(img2)
    substract_images(clean_img1,clean_img2)
    extract_fields("../meta-data/pre-result.jpg")

    #cleanup()
