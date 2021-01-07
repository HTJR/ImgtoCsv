import cv2
import numpy as np
import numpy as npThank
from PIL import Image, ImageOps
import pytesseract
from pdf2image import convert_from_path
import pandas as pd 
import argparse
import os
from helper import tocsv
path=r"poppler-20.12.1\Library\bin"


parser = argparse.ArgumentParser(
    description='Program to cinvert tables from images to csv format')
parser.add_argument("--IPFILE", default="*.pdf",
                                  help='Table from PDF or Image: '
                                       )
parser.add_argument("--OPFILE", default="Output.csv",
                                  help='Name of Output file: '
                                       )

args = parser.parse_args()

def conv(pages):
    Head = False
    for page in pages:
        frame=np.asarray(page)
        te,col=tocsv(frame)
        if Head is False:
            df = pd.DataFrame(te,columns=col)
        else:
            df=pd.DataFrame(te)
        if Head is False:
            df.to_csv(args.OPFILE,mode='a',index=False)
            Head = True
        else:
            df.to_csv(args.OPFILE, mode='a', header=False,index=False)

def conv1(ip):
    te,col=tocsv(ip)
    df = pd.DataFrame(te,columns=col)
    df.to_csv(args.OPFILE,mode='a',index=False)


filename, file_extension = os.path.splitext(args.IPFILE)
if file_extension == ".pdf":
    pages1 = convert_from_path(args.IPFILE,poppler_path = path)
    conv(pages1)
else:
    ip1=cv2.imread(args.IPFILE)
    conv1(ip1)
