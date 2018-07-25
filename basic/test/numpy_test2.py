import numpy as np

a = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(np.shape(a))
b = np.reshape(a,[1,3,1,3])
print(b)
print(np.shape(b))
c = b[:,:,:,0]
print(c)
print(np.shape(c))