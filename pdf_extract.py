from pdf2image import convert_from_path
import os
import sys
import re
import imp_stat

pdf_path =input("Enter pdf path:")
images = convert_from_path(pdf_path, 500,poppler_path=r'C:\\Program Files\\poppler-22.01.0\\Library\\bin')
name = input("Enter name for the output file:")

def pdf_extract(pdf_path,images,name):
    pass
for i in range(len(images)):
    path='E:\\Assignments\\OCR\\Data\\'
    filename = name+str(i)+'.jpg'
    fullpath = os.path.join(path, filename)
    images[i].save(fullpath)
print(fullpath)
 
   









   
#file1=open(r"E:\\Assignments\\OCR\\4.jpg","a")
#file1.save(images)

#for i in range(len(images)):
#   images[i].save('page' + str(i) +'.jpg','JPEG')

#images[i].save('page' + str(i) +'.jpg','JPEG')
#images[i].os.path.join(save_path,'page' + str(i) +'.jpg','JPEG')