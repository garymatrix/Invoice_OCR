import io
import pytesseract
from PIL import Image
import re 
import imp_stat

img_path =input("Enter image path:")

def OCR(img_path):
	pass
name = input("Enter output file's name:")
file = Image.open(img_path,'r') 
string = pytesseract.image_to_string(file, lang='eng')
with open ('Data/'+name+'.txt','w') as f:
	print(string,file=f)

#print(string)













"""
for i in range(len(str)):
	path='E:\\Assignments\\OCR\\Data\\'
	filename = str(i)+'.txt'
	fullpath = os.path.join(path, filename)
	images[i].save(fullpath)
"""

