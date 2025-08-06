import numpy as np
"""
# creating 1D arrays

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.shape)


# creating 2D arrays

arr2 = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2)
print(arr2.shape)




# conversion of arrays 1D to 2D

np.arange(0,10,2).reshape(5,1)

np.eye(3)  # identical matrix
np.ones((2,3))  # give 2 rows 3 colomn and element are all ones.

# Attribute of numpy

print("Arrays:", arr2)
print("shape:", arr2.shape)
print("no of dim:", arr2.ndim)
print("size(no of element):", arr2.size)
print("Datatype:", arr2.dtype)
print("Itemsize(in byts):", arr2.itemsize)
"""

# Array vectorized operation
"""
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])
"""
"""print("Addision:", arr1 + arr2)  
print("Subtraction:", arr2 - arr1)
print("Multiplication:", arr1 * arr2)
print("Division:", arr2 / arr1)

"""

# Universal function
"""
arr = np.array([2,3,4,5,6,7,8,9])

print(np.sqrt(arr))  #Square rooot
print(np.exp(arr))   #Exponential
print(np.sin(arr))   #Sign Function
print(np.log(arr))   #Natural log
"""
# array slicing and Indexing

arr = [[(1,2,3,4,5),(6,7,8,9,10),(11,12,13,14,15)]]
print("Array : \n", arr)
print(arr[0][0])  # use for accesing element in 01st rows.
print(arr[1:2:])  #  "  "     "       "      in other rows.


# Normalization --> converting of data in format of mean =0 and sd = 1
"""
data = np.array([1,2,3,4,5,6])

# calcualte Mean
mean = np.mean(data)
std_dev = np.std(data)

# Normalized data
normalized_data = (data - mean) / std_dev
print("normalized data:", normalized_data)

"""

# Basic calculations
"""
data = np.array([1,2,3,4,5,6,7,8,9,10])

# Mean
mean = np.mean(data)
print("Mean:", mean)

# Median
median = np.median(data)
print("Median:", median)

# Standard deviation

std_dev = np.std(data)
print("Standrd deviation:", std_dev)

# variance
variance = np.var(data)
print("variance:", variance)"""

# Logical operation
"""
data = np.array([1,2,3,4,5,6,7,8,9,10])
print(data[data>5])  # print only those value which is greater than 5. (condition)
print(data[(data>=5) & (data<=8)])  # (this is also condition)
"""


