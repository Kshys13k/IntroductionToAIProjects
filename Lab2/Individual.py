import copy
import numpy as np
from cec2017.functions import f1, f2, f3
import matplotlib.pyplot as plt
class Individual:
    def __init__(self, genes, score=None):
        self.genes=genes
        if score==None:
            self.calculateScore()
        else:
            self.score=score
    def __str__(self):
        return str(self.genes)+ "; score: " + str(self.score)
    def calculateScore(self):
        self.score=f1(self.genes)[0]
        return self.score