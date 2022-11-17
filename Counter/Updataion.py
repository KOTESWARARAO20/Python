# A Python program to demonstrate update()
from collections import Counter

coun = Counter()

coun.update([1, 2, 3, 1, 2, 1, 1, 2])
print(coun)

coun.update([1, 2, 4])
print(coun)



#ex:sub
from collections import Counter

c1 = Counter(A=4, B=3, C=10)
c2 = Counter(A=10, B=3, C=4)

c1.subtract(c2)
print(c1)