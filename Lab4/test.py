from ID3 import ID3
import pandas as pd
import numpy as np

df=pd.read_csv("smallDataSet.csv", header=None)

df=df.rename(columns={0:"class",1:"pogoda", 2:"wiatr", 3:"pora"})
dataClass=df.iloc[:,0:1]
data=df.iloc[:,1:]

id3=ID3()
id3.train(data,dataClass)

# df=pd.concat([data,dataClass], axis=1)
#
# uniqueValues=["no-recurrence-events","recurrence-events"]
# r=ID3.calcInfoGain("age",df,uniqueValues)
# print(r)
