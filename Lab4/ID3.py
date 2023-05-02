import pandas as pd
import numpy as np


class Node:
    def __init__(self, id, myParameter, parent=None):
        self.id=id
        self.parent=parent
        self.isLeaf=False
        self.value = ""
        self.children = {} #Parametr value: node
        self.myParameter=myParameter


class Tree:
    nodeList=[]
    maxNodeNumber=-1

    def addNode(self, parameter, parentId=0, parentValue=""): #node parameter, id of parent, value of parameter in parrent that lead to this node
        if self.maxNodeNumber==-1:
            node= Node(0, parameter)
            self.nodeList.append(node)
            self.maxNodeNumber=0
        else:
            node= Node(self.maxNodeNumber+1, parameter, self.nodeList(parentId))
            self.nodeList.append(node)
            parentNode=self.nodeList(parentId)
            parentNode.children[parentValue]=node
            self.maxNodeNumber+=1

    def getChildEqualValue(self, id, value):
        currentNode=self.nodeList(id)
        for childValue in currentNode.children:
            if value == childValue:
                return currentNode.children[value].id





class ID3:
    def __init__(self,df):
        pass

    #given: subdataset contains only answears column to calculate entropy, unique answears
    #return: entropy of one parameter
    @staticmethod
    def __calcEntropy(subDf, uniqueValues):
        numberOfRows = subDf.shape[0]
        totalEntropy = 0.0
        for value in uniqueValues:
            count = subDf[subDf.iloc[:, 0] == value].shape[0]
            subEntropy=0
            if count != 0:
                subEntropy = -(count / numberOfRows) * np.log2(count / numberOfRows)
            totalEntropy += subEntropy
        return totalEntropy

    @staticmethod
    def calcInfoGain(parameterName, df, uniqueValues):
        df=df[[parameterName, df.columns[-1]]]

        #calculateTotalEntropy
        dfTotalEntropy=df.iloc[:,1:2]
        totalEntropy=ID3.__calcEntropy(dfTotalEntropy, uniqueValues)

        #calculate parameter info
        parameterUniqueValues=df.iloc[:,0].unique()
        numberOfRows=df.shape[0]
        parameterInfo=0.0
        for parameterValue in parameterUniqueValues:
            dfSpecificValue= df[df.iloc[:,0]==parameterValue]
            specificValueCount=dfSpecificValue.shape[0]
            dfSpecificValue=dfSpecificValue.iloc[:,1:2]
            subEntropy=ID3.__calcEntropy(dfSpecificValue, uniqueValues)
            specificValueProbability=specificValueCount/numberOfRows
            parameterInfo+=subEntropy * specificValueProbability
        infoGain=totalEntropy-parameterInfo
        return infoGain


    def train(self, trainingDataSet, answears):
        answears.columns=["answears"]
        #uniqueValues= unique answears
        df=pd.concat([trainingDataSet, answears], axis=1)

        #check if all answears are the same
        if df["answears"].nunique()==1:
            pass

        #check if number of parameters is 0
        if df.shape[1]==1:
            pass


    def predict(self):
        pass