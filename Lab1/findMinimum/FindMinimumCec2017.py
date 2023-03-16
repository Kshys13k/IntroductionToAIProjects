import copy
import numpy as np
from cec2017.functions import f1, f2, f3
import matplotlib.pyplot as plt

class FindMinimumCec2017:
    def numericGradient(self, func, args):
        EPSILON=1e-10
        gradientTable=[]
        for i in range (len(args[0])):
            argsCopy=copy.deepcopy(args)
            argsCopy[0][i]-=EPSILON
            gradient=((func(args)-func(argsCopy))/EPSILON)
            gradientTable.append(*gradient)
        return gradientTable

    def gradientDescent(self,func, args, learningRate, maxIteration):
        for i in range(0, maxIteration):
            gradTable=self.numericGradient(func, args)
            for i in range(len(args[0])):
                args[0][i]=args[0][i]-learningRate*gradTable[i]
        return args, func(args)

    def gradientDescentVerbose(self,func, args, learningRate, maxIteration):
        for i in range(0, maxIteration):
            gradTable=self.numericGradient(func, args)
            for i in range(len(args[0])):
                args[0][i]=args[0][i]-learningRate*gradTable[i]
            print("X1: " + str(args[0][0])+ " X2: "+ str(args[0][1])+ " f= "+ str(func(args)))
        return args, func(args)

    def gradientDescentPlot(self,func, args, learningRate, maxIteration):
        MAX_X = 100
        PLOT_STEP = 1
        x_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
        y_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
        Xplot, Yplot = np.meshgrid(x_arr, y_arr)
        Z = np.empty(Xplot.shape)
        argsCopy=copy.deepcopy(args)
        for i in range(Xplot.shape[0]):
            for j in range(Xplot.shape[1]):
                argsCopy[0][0]=Xplot[i, j]
                argsCopy[0][1]=Yplot[i, j]
                Z[i, j] = func(argsCopy)
        levels = []
        # for i in range(0, 1000, 2000): levels.append(i)
        plt.contourf(Xplot, Yplot, Z, 75, cmap="rainbow")
        plt.contour(Xplot, Yplot, Z, 75, colors="black")

        for i in range(0, maxIteration):
            gradTable=self.numericGradient(func, args)
            for i in range(len(args[0])):
                x1=args[0][0]
                x2=args[0][1]
                args[0][i]=args[0][i]-learningRate*gradTable[i]
            plt.arrow(args[0][0], args[0][1], x1-args[0][0], x2-args[0][1], head_width=0.3, head_length=0.3, fc='k', ec='k')
        plt.show()
        return args, func(args)


# samples=1
# dimension=20
# x = np.random.uniform(-100, 100, size=(samples, 20))
# gradientDescentPlot(f3,x,1e-10,1000)



