
import Lab1.cec2017
import numpy as np

from Lab1.cec2017.functions import f1

UPPER_BOUND = 100
DIMENSIONALITY = 2
#wylosuj punkt x:
x = np.random.uniform(0, UPPER_BOUND, size=DIMENSIONALITY)

#wyznacz ocenę x
q = f1(x)
print('q(x) = %.6f' %q)