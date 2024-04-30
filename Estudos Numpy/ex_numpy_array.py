import numpy as np
'''#NumPy Array
#1-D
arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))

#2-D
mtz = np.array([[1, 2], [3, 4]])
print(mtz)

#estruturando numpy arrays

#ones
mtz = np.ones([5,5])
print(mtz)

#zeros
arr = np.zeros(10)
print(arr)

#arange
arr = np.arange(20, 30, 1).reshape(2,5)
print(arr)
'''
#Operações entre numpy arrays
jan = np.arange(20, 30, 1)
feb = np.arange(40, 50, 1)

print(jan,feb)

print(jan+feb) #somar
print(np.concatenate([jan,feb]).reshape(5, 4)) #concatenar

#tamanho de um ndarray
print(jan.size)
print(jan.ndim)
print(jan.shape)

