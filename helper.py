import cv2
import numpy as np
import numpy as npThank
from PIL import Image, ImageOps
import pytesseract
import pandas as pd 

pytesseract.pytesseract.tesseract_cmd = r'D:\tess\tesseract'



def box_extraction(img_for_box_extraction_path):
    gray = cv2.cvtColor(img_for_box_extraction_path, cv2.COLOR_BGR2GRAY)
    
    img = gray
    (thresh, img_bin) = cv2.threshold(img, 128, 255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Thresholding the image
    img_bin = 255-img_bin  # Invert the image
    kernel_length = np.array(img).shape[1]//40
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
    verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
    return verticle_lines_img,horizontal_lines_img


def retline(gray):
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
    return lines


def tocsv(ip):
    frame=ip
    v,h=box_extraction(frame)
    l=retline(v)# getting all the vertivle line coordinates
    li=retline(h)#getting all the horizontal line coordinates
    p=[]
    for ij in l:
        p.append(ij[0][0])
    p.sort()
    # this block finds the first horizontal line and last horizontal line
    min1=li[0][0][1]
    max1=0
    for ii in li:
        te=ii[0][1]
        if te<min1:
            min1=te
        if te>max1:
            max1=te

    # op will store all the coulmns which will be cropped this will work on more than 2 coulmns also
    im_pil = Image.fromarray(frame)
    pt=p[0]
    op=[]
    for j in range(1,len(p)):
        crop_img =im_pil.crop((pt, min1, p[j], max1))
        pt=p[j]
        im_np = np.asarray(crop_img)
        op.append([pytesseract.image_to_string(im_np)])

    te=[]
    for jj in op:
        if jj[0] is not '\x0c':
            te.append([k for k in jj[0].split("\n") if len(k)>1])

    te=list(map(list, zip(*te)))
    col=te[0]
    te.pop(0)
    return te,col

if __name__ == "__main__":
    pass