import numpy as np

a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
b = a            # no new object is created
print(b is a)           # a and b are two names for the same ndarray object
c = a.view()
print(c is a)
print(c.base is a)          # c is a view of the data owned by a
print(c.flags.owndata)
c = c.reshape((2, 6))  # a's shape doesn't change, reassigned c is still a view of a
print(a.shape)
c[0, 4] = 1234         # a's data changes
print(a,"\n")
s = a[:, 1:3]
s[:] = 10  # s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
print(a)

#---correct way to copy---
d = a.copy()  # a new array object with new data is created
print(d is a,d.base is a) # d doesn't share anything with a
d[0, 0] = 9999
print("a:\n",a)
print("d:\n",d)
#--incase worry about mem--
a = np.arange(int(1e5))
b = a[:100].copy()
del a  # the memory of ``a`` can be released.