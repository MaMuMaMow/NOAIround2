import numpy as np
import sys

a = np.arange(15).reshape(3,5)
print(a)
print(a.shape,a.ndim,a.itemsize,"\n")

b = np.array([1,2,3,4])
print(b.dtype)

z = np.zeros((3,4))
o = np.ones((2,3))
print(z,"\n\n",o)

inc1 = np.arange(10,30,5) #int
print(inc1,"\n")

inc2 = np.linspace(0,2,9) #float
print(inc2,"\n")

#a.reshape(1,15)
#print(a,a.shape,"\n")

#in case dont want numpy to skip printing a large arr
#np.set_printoptions(threshold=sys.maxsize)



"""
normal operators
a = np.array([20, 30, 40, 50])
b = np.arange(4)
b
c = a - b
c
b**2
10 * np.sin(a)
a < 35

Products operators
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
A * B     # elementwise product
A @ B     # matrix product
A.dot(B)  # another matrix product
"""
print(a.sum(axis=0),a.min(axis=1)) #0 is column, 1 is rows
print(a.cumsum(axis=1))
