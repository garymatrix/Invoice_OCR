import pandas as pd
path = 'E:\\Assignments\\OCR\\data\\M10.txt'

#print(data.head())

file = open(path,'r')
lines = file.readlines()

df = pd.read_csv(path,sep=' ',header=None)
print(df)