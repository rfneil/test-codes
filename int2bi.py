
import numpy as np
int2binary = {}
binary_dim = 4

largest_number = pow(2,binary_dim)
binary = np.unpackbits(np.array([range(largest_number)], dtype=np.uint8).T,axis=1)
for i in range(largest_number):
		int2binary[i] = binary[i]
print (str(int2binary)+"\n")
