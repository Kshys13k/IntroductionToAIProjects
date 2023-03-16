from _decimal import Decimal
import numpy as np
from cec2017.functions import f1, f2, f3
import matplotlib.pyplot as plt

def numericGradient(func, args):
    EPSILON=1
    gradientTable=[]
    argsCopy=args
    for i in range (len(args[0])):
        args=argsCopy
        args[0][i]-=EPSILON
        print("dupa")
        print(func(argsCopy))
        print(func(args))
        gradient=Decimal(((func(argsCopy)-func(args))/EPSILON)[0])
        print(gradient)
        print(type(gradient))
        gradientTable.append(gradient)
    return gradientTable

samples=1
dimension=2
x = np.random.uniform(-100, 100, size=(samples, dimension))
print(x)
print(f1(x))
print(numericGradient(f1,x))