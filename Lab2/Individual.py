import copy
import numpy as np
from cec2017.functions import f4, f5
import matplotlib.pyplot as plt
class Individual:
    def __init__(self, genes, score=None, functionNumber=4):
        self.genes=genes
        self.functionNumber=functionNumber
        if score==None:
            self.calculateScore(functionNumber)
        else:
            self.score=score
    def __str__(self):
        return str(self.genes)+ "; score: " + str(self.score)
    def calculateScore(self, functionNumber):
        if functionNumber==4:
            self.score=f4(self.genes)[0]
        if functionNumber==5:
            self.score = f5(self.genes)[0]
        return self.score