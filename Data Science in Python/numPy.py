# Week: 1
# Lesson: Python Demonstration: The Numerical Python Library (NumPy)
# Date Started: 19 May 2020
# Date Finished: 19 May 2020

# import numpy
import numpy as np

# create a multidimensional array through lists of lists
mylist = [1,2,3]
x = np.array(mylist)
y = np.array([4,5,6])
m = np.array([[7,8,9],[10,11,12]])
print(x)
print(y)
print(m)

# count rows, columns
print("The shape of the first array is:"+str(x.shape))
print("The shape of the second array is:"+str(m.shape))

# arange using (start, stop, stepsize)
n = np.arange(10, 20, 3)
print(n)

# and reshape to temporarily change presentation
n = n.reshape(2, 2)
print(n)

# or: range and number of values wanted to split up accordingly
o = np.linspace(10, 20, 4)
print(o)

# resize to change data organization permanently
o.resize(2, 2)
print(o)

# create arrays of 1s and 0s
p = np.ones((5,7))
print(p)
q = np.zeros((4,3))
print(q)
r = np.eye(5)
print(r)
s = np.diag(x)
print(s)

# create arrays through * or through repeat
t = np.array([1,2,3] * 3)
print(t)
u = np.repeat([1,2,3],3)
print(u)

# stack arrays vertically and horizontally
v = np.ones([2,3], int)
print(v)
w = np.vstack([v, 2*v])
print(w)
x = np.hstack([v, 2*v])
print(x)

# OPERATIONS
print(t)
y = np.array([t, t**2])
print(y)

# swap rows and columns
z = y.T
print(z)

# see what data types a certain array has, and change the data type
a = z.dtype
print(a)
b = z.astype("f")
print(b)

# determine sum, max, min, mean, and std deviation
c = np.array([1,4, -2, 15, 3, 0])
print(c.sum(), c.max(), c. min(), c.mean(), c.std())

# INDEXING/SLICING

# find array values at certain indices
d = np.arange(13)**2
print(d)
print(d[0], d[3], d[2:6])
print(d[-5: :-2])

e = np.arange(36)
e.resize((6,6))
print(e)
print(e[2,2])

