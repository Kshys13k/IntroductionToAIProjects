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

    def __str__(self):
        try:
            parent = str(self.parent.id)
        except:
            parent = "None"
        if self.isLeaf:
            s = "Leaf, id: " + str(self.id) + ", myParam: " + str(self.myParameter) + ", parentId: " + str(parent) + ", value: " + str(self.value)
        else:
            strChildrenIds="("
            for child in self.children.keys():
                strChildrenIds += str(self.children.get(child).id)
                strChildrenIds += ": "
                strChildrenIds+=str(child)
                strChildrenIds += ", "
            strChildrenIds+=")"
            s = "Branch, id: " + str(self.id) + ", myParam: " + str(self.myParameter) + ", parentId: " + str(parent) + ", children: " + strChildrenIds

        return s


class Tree:
    def __init__(self):
        self.nodeList = []
        self.maxNodeNumber = -1
    def addNode(self, parameter, parentId, parentValue): #node parameter, id of parent, value of parameter in parrent that lead to this node
        if self.maxNodeNumber==-1:
            node= Node(0, parameter)
            self.nodeList.append(node)
            self.maxNodeNumber=0
        else:
            parent=self.nodeList[parentId]
            node= Node(self.maxNodeNumber+1, parameter, parent)
            self.nodeList.append(node)
            parentNode=self.nodeList[parentId]
            parentNode.children[parentValue]=node
            self.maxNodeNumber+=1
        return self.maxNodeNumber #return Id of new node

    def getChildEqualValue(self, id, value):
        currentNode=self.nodeList(id)
        for childValue in currentNode.children:
            if value == childValue:
                return currentNode.children[value].id

    def getLastNode(self):
        return self.nodeList[self.maxNodeNumber]

    def printTree(self):
        for node in self.nodeList:
            print(node)


class ID3:
    def __init__(self):
        self.tree=Tree()

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
    def __calcInfoGain(parameterName, df, uniqueValues):
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

    @staticmethod
    def __findBestParameter(df, uniqueValues):
        parametersList=list(df.columns)

        maxInfoGain=-1
        maxInfoParameter=None

        for param in parametersList:
            infoGain=ID3.__calcInfoGain(param, df, uniqueValues)
            if infoGain>maxInfoGain:
                maxInfoGain=infoGain
                maxInfoParameter=param

        return maxInfoParameter

    def id3main(self, df, parentId=None, parentValue="", dfOryginal=None):
        if dfOryginal is None:
            dfOryginal=df.copy()
        uniqueValues = list(df["answears"].unique())
        #check if all answears are the same:
        if df["answears"].nunique()==1:
            parameter=df.columns[0]
            self.tree.addNode(parameter,parentId,parentValue)
            node=self.tree.getLastNode()
            node.isLeaf=True
            node.value = df.iloc[0,-1]
        #check if number of parameters is 0:
        elif df.shape[1]==1:

            parameter=None
            self.tree.addNode(parameter, parentId, parentValue)
            mostCommonValue = df["answears"].value_counts().idxmax()
            node = self.tree.getLastNode()
            node.isLeaf = True
            node.value = mostCommonValue

        # if this is not a leaf create new branches:
        else:
            dfParameters=df.drop(columns="answears")
            bestParameter=ID3.__findBestParameter(dfParameters, uniqueValues)
            myId=self.tree.addNode(bestParameter,parentId,parentValue)
            parameterValues=list(dfOryginal[bestParameter].unique())
            for value in parameterValues:
                childDf=df[df[bestParameter]==value]
                childDf=childDf.drop(columns=[bestParameter])
                #t
                if childDf.shape[0] == 0:
                    childDf = pd.DataFrame(df["answears"])

                self.id3main(childDf,myId,value, dfOryginal)

    def train(self, trainingDataSet, answears):
        answears.columns = ["answears"]
        df = pd.concat([trainingDataSet, answears], axis=1)
        parentId = None
        parentValue = ""
        self.id3main(df,parentId,parentValue)
        self.tree.printTree()

    def readTree(self, row, node):
        if node is None:
            return "noData"
        if node.isLeaf:
            return node.value
        parameter=node.myParameter
        col=pd.DataFrame(row.loc[:,parameter])
        parameterValue=col.iloc[0,0]
        child=node.children.get(parameterValue)
        return self.readTree(row,child)
    def predict(self,df):
        root=self.tree.nodeList[0]
        newCol=[]
        for i in range (df.shape[0]):
            rowDf=df.iloc[i:i+1,:]
            newCol.append(self.readTree(rowDf, root))
        dictionary = {"Predictions": newCol}
        df2 = pd.DataFrame(dictionary)
        return df2