import matplotlib.pyplot as plt
import numpy as np
def BoothFunction(x,y):
    return (x+2*y-7)**2+(2*x+y-5)**2
def BoothFunctionXDerivative(x,y):
    return 10*x+8*y-34
def BoothFunctionYDerivative(x, y):
    return 8*x+10*y-38

def gradientDescent(X,Y,learningRate, maxIteration, epsilon):
    for i in range (0,maxIteration):
        print(str(X) + " " + str(Y) + " " + str(BoothFunction(X, Y)))
        X=X-(learningRate*BoothFunctionXDerivative(X,Y))
        Y=Y-(learningRate*BoothFunctionYDerivative(X,Y))
        if(BoothFunction(X,Y)<epsilon):
            maxIteration=i
            break
    return X, Y, BoothFunction(X,Y), maxIteration

def gradientDescentPlot(X,Y,learningRate, maxIteration, epsilon):
    #creating plot:
    MAX_X = 10
    PLOT_STEP = 0.1
    x_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
    y_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
    Xplot, Yplot = np.meshgrid(x_arr, y_arr)
    Z = np.empty(Xplot.shape)
    for i in range(Xplot.shape[0]):
        for j in range(Xplot.shape[1]):
            arg = np.array([Xplot[i, j], Yplot[i, j]])
            Z[i, j] = BoothFunction(*arg)
    levels = []
    for i in range(0, 50, 2000): levels.append(i)
    plt.contourf(Xplot,Yplot,Z,20, cmap="rainbow")
    plt.contour(Xplot, Yplot, Z, 20, colors="black")

    #gradient descend algorithm:
    for i in range (0,maxIteration):
        X1 = X
        Y1 = Y
        X=X-(learningRate*BoothFunctionXDerivative(X,Y))
        Y=Y-(learningRate*BoothFunctionYDerivative(X,Y))
        plt.arrow(X1, Y1, X-X1, Y-Y1, head_width=0.5, head_length=1, fc='k', ec='k')
        if(BoothFunction(X,Y)<epsilon):
            maxIteration=i
            break

    plt.show()
    return X, Y, BoothFunction(X,Y), maxIteration
print(gradientDescentPlot(9,9, 0.1, 10000, 0.1))