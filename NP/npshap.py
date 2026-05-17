import numpy as np

a = np.arange(16).reshape(8,-1) #-1 is automatically calculate the dimension
print(a)
print(a.T)

a.resize(4,4)
print(a)
