import numpy as np

#creating array

a=np.array([1,2,3,4,5])
print (a)
print(type(a))
print("________")
# 4. Arrays consume less memory than list.

import sys
l = [10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100]
a = np.array([10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100])
print('The Size of list l => ',sys.getsizeof(l))
print('The Size of ndarray a => ',sys.getsizeof(a))

#ex2 more than one dim
a1=np.array([[1,5,3],[5,6,52]])
print(a1)
print("__________")
#dtype parameter
a2=np.array([1,2,4],dtype=complex)
print(a2)
#shape of the array tuples it will return in tuple


#Numpy attributes
print(a1.shape)#2 rows and 3 col
print("----------")
#resize of the nd array
a4=np.array([[1,2,4],[9,0,8]])
print(a4.shape)
a4.shape=(3,2)
print(a4)
print("----------")
#chaning the shap
ko=a4.reshape(2,3)
print(ko)

print("----------")


#ex5
#1d array
a5=np.arange(24)
print(a5)
b=a5.reshape(2,4,3)#2 matrix 4 rows and 3 col
print(b)



print("----------")

#ex5 item size it willll returns the length of each element of array in bytes
jk=np.array([[20,30,50],[20,4,5]],dtype=np.int8)
print(jk.itemsize)










