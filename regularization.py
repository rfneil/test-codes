import numpy as np

a = np.array([[0.7],[2],[3],[4]])
d = np.random.rand(a.shape[0],a.shape[1]) < 0.8
a = np.multiply(a,d)
print a
print d
