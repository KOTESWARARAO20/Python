import numpy as np

# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])
print("Array is of type: ", type(arr))
print("No. of dimensions: ", arr.ndim)
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)
print("Array is: ")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i,j],end="  ")
    print()
