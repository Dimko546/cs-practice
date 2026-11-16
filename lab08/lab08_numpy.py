import numpy as np


hours = np.array([i for i in range(0,22,3)])
line = np.array([0, 0.25, 0.5, 0.75, 1])
zeros = np.array([0 for i in range(6)])
unknown_table = np.array([[-1 for i in range(2)],
                [-1 for i in range(2)],
                [-1 for i in range(2)]
])
identity = np.array([[1,0,0],
                     [0,1,0],
                     [0,0,1]
])

print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)


print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])


temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)

print(temperatures[1,2])
print(temperatures[0])
print(temperatures[:,-1])
print(temperatures[0:2,1:])
print(temperatures[0:2,1:3])


matrix = np.arange(1, 26).reshape(5, 5)

print(matrix[0:3])
print(matrix[0:3].shape)
print(matrix[-2:])
print(matrix[-2:].shape)
print(matrix[:,0:2])
print(matrix[:,0:2].shape)
print(matrix[1:4,2:5])
print(matrix[1:4,2:5].shape)
print(matrix[-2:,-2:])
print(matrix[-2:,-2:].shape)


changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print(changed_hours)
print(hours)
#.copy() нужна чтобы не потерять изначальный список

changed_matrix = matrix.copy()
changed_matrix[1,:] = 0
changed_matrix[:,-1] = -1
changed_matrix[1:4,1:4] = 100
print(changed_matrix)
print(matrix)


numbers = np.arange(12)
table = numbers.reshape(3,4)
transposed = table.T
print(numbers.shape)
print(table.shape)
print(transposed.shape)
#reshape(5,3) вызывает ошибку потому что в numbers
#не хватает элементов для преобразования в (5,3)