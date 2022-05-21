import os
import sys
import re
import imp_stat
import io
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

path =input("Enter your File's name:")
img = convert_from_path(path, 500,poppler_path=r'C:\\Program Files\\poppler-22.01.0\\Library\\bin')
otp = input("Enter name for the output file:")

def pdf_extract(pdf_path,images,name):
 for i in range(len(images)):
    path='E:\\Assignments\\OCR\\Data\\'
    filename = name+str(i)+'.jpg'
    fullpath = os.path.join(path, filename)
    images[i].save(fullpath)
 return fullpath
    


def OCR(fullpath, name):
 img_path = fullpath
 file = Image.open(img_path,'r') 
 string = pytesseract.image_to_string(file, lang='eng')
 with open ('Data/'+name+'.txt','w') as f:
    print(string,file=f)

pdf_extract(path,img,otp)
fpath = pdf_extract(path,img,otp)
OCR(fpath,otp)