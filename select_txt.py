import os
import sys
import re
import imp_stat


txt_path =input("Enter path for the text file:") #'E:\\Assignments\\OCR\\Data\\0.txt'
file = open(txt_path,'r')
lines = file.readlines()

for index, line in enumerate(lines):
      lines[index] = line.strip()
      
for line in lines:
    if re.findall(r"^Invoice number", line, re.IGNORECASE):
     print(line)
    elif re.search(r"^INVOICE", line, re.IGNORECASE):
        print(line)
    elif re.search(r"^Tax Invoice", line, re.IGNORECASE):
        print(line)
    elif re.search(r"^Purchase Order", line, re.IGNORECASE):
        print(line)             
    elif re.search(r"^Proforma Invoice", line, re.IGNORECASE):
        print(line)
    elif re.findall(r"^GSTN No|GSTIN|GSTIN/UIN+\d.*\d",line, re.IGNORECASE):
        print(line)
    #elif re.search("^Address ",line, re.IGNORECASE):
       # print(line)
    elif re.findall(r"^Bill Number|Invoice Number+\d.*\Z",line, re.IGNORECASE):
        print(line)
    elif re.search(r"^Due Date+\d$" ,line, re.IGNORECASE):
        print(line)
    elif re.search(r"^From | Seller Name ",line, re.IGNORECASE):
        print(line)
    #elif re.search(r"^To",line, re.IGNORECASE):
        #print(line)
    elif re.search(r"^Line item| Item",line, re.IGNORECASE):
        print(line)
    elif re.findall(r"^Tax Reference Number ",line, re.IGNORECASE):
        print(line)
    elif re.search(r"^Tax amount",line, re.IGNORECASE):
        print(line)
    elif re.search(r"^Total",line, re.IGNORECASE):
        print(line)
    elif re.search(r"^For.*Limited|Ltd\Z",line, re.IGNORECASE):
        print(line)
    elif re.search(r"^To.*\d\Z",line, re.IGNORECASE):
        print(line)
    elif re.search(r"^INR.*\d+only\Z",line, re.IGNORECASE):
        print(line)
    #elif re.search(r"^.*\d+\Z",line, re.IGNORECASE):
        #print(line)
    elif re.search(r"^\d.*\d+\Z",line, re.IGNORECASE):
        print(line)
print("\nOutput Generated Sucessfully")









'''
Below are the fields for output.
elif re.search(r"^.*\d+\Z",line, re.IGNORECASE):
Invoices : 
Type of Document: Invoice. Tax Invoice, Purchase Order, Proforma Invoice
Seller Name, GSTIN 
Buyer Name, GSTIN
Bill Number or Invoice Number
Bill Date or Invoice Date
Due Date
Invoice ammount 
Total 
(other details Line item, Taxable Value, tax amount)

'''
'''
for element in Doc_typ:
    z = re.match(r"(g\w+)", element, re.IGNORECASE)
    if z:
        print(z.groups())
'''
'''
#lines = raw.rstrip()
var = ''
raw_list =["Invoice","Tax Invoice","Purchase Order","Proforma Invoice" ]
Doc_typ = ' '.join([x for x in raw_list])

def search(lines, Doc_typ):
    pass
x =  re.search(lines, Doc_typ)
print(x.group())

'''
