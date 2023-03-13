import numpy as np
# Using only f5:
from cec2017.functions import f5
samples = 1
dimension = 10
x = np.random.uniform(-100, 100, size=(samples, dimension))
print(type(x))
print(x.shape)
print(x)
val = f5(x)
for i in range(samples):
    print(f"f5(x_{i}) = {val[i]:.6f}")

# Using all functions:
from cec2017.functions import all_functions
for f in all_functions:
    x = np.random.uniform(-100, 100, size=(samples, dimension))
    val = f(x)
    for i in range(samples):
        print(f"{f.__name__}(x_{i}) = {val[i]:.6f}")