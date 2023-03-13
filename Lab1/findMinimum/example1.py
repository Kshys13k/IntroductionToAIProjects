import numpy as np

from cec2017.functions import f1

#exemple code from laboratory instruction (it has been modified so it works)

samples = 1
UPPER_BOUND = 100
DIMENSIONALITY = 2
#pick random x:
x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=(samples,DIMENSIONALITY))

#print f(x)
q = f1(x)
print('q(x) = %.6f' %q)