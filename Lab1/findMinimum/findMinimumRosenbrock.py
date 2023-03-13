
def RosenbrockFunction(x,y):
    return (1-x)**2+100*(y-x**2)**2
def RosenbrockFunctionXDerivative(x,y):
    return 400*x**3-400*x*y+2*x-2
def RosenbrockFunctionYDerivative(x,y):
    return 200*(y-x**2)

#prints all steps of gradient descent algorithm for Rosenbrock function; returns X,Y cordinates of solution, solution and number of steps
def gradientDescent(X,Y,learningRate, maxIteration, epsilon):
    for i in range (0,maxIteration):
        print(str(X) + " " + str(Y) + " " + str(RosenbrockFunction(X, Y)))
        X=X-(learningRate*RosenbrockFunctionXDerivative(X,Y))
        Y=Y-(learningRate*RosenbrockFunctionYDerivative(X,Y))
        if(RosenbrockFunction(X,Y)<epsilon):
            maxIteration=i
            break
    return X, Y, RosenbrockFunction(X,Y), maxIteration


gradientDescent(3,1, 1e-6, 10000, 0)