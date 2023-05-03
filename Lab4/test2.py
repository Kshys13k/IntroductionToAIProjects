from ID3 import ID3
import pandas as pd
import numpy as np

df=pd.read_csv("breast-cancer.csv", header=None)

df=df.rename(columns={0:"class",1:"age", 2:"menopause", 3:"tumor-size", 4:"inv-nodes", 5:"node-caps", 6:"deg-malig",7:"breast", 8:"breast-quad",9:"irradiat"})
dataClass=df.iloc[:,0:1]
data=df.iloc[:,1:]

id3=ID3()
id3.train(data,dataClass)
ans=id3.predict(data)
print(ans)
print(dataClass)
good=0
bad=0
for i in range(ans.shape[0]):
    row1 = ans.iloc[i, 0]
    row2 = dataClass.iloc[i, 0]
    if row1 == row2:
        good+=1
    else:
        bad+=1
print("good: "+ str(good) + ", bad: "+ str(bad))