from ID3 import ID3
import pandas as pd
import numpy as np

df=pd.read_csv("breast-cancer.csv", header=None)

df=df.rename(columns={0:"class",1:"age", 2:"menopause", 3:"tumor-size" , 4:"inv-nodes" , 5:"node-caps" , 6:"deg-malig" , 7:"breast" , 8:"breast-quad" , 9:"irradiat"})
dataClass=df.iloc[:,0]
data=df.iloc[:,1:]
df=pd.concat([data,dataClass], axis=1)

uniqueValues=["no-recurrence-events","recurrence-events"]
r=ID3.calcInfoGain("age",df,uniqueValues)
print(r)
