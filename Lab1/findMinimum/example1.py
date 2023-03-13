import numpy as np

from cec2017.functions import f1

samples = 1
UPPER_BOUND = 100
DIMENSIONALITY = 2
#wylosuj punkt x:
x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=(samples,DIMENSIONALITY))

#wyznacz ocenę x
q = f1(x)
print('q(x) = %.6f' %q)