import pandas as pd
import numpy as np

s=pd.Series()#creating Series dS whicch is stored in s

print(s)#Series([],dtype:float 64),empty series created with floating point of 64


data=np.array(['hyd','che','pune','mum'])
s1=pd.Series(data)#numpy array is given input to series DS
print(s1)
print(type(s1))


arr1=np.array([11,222,32,42,522])
ser1=pd.Series(arr1)
print(ser1)

print("____________-_____________")


#Example2:


s0=pd.Series(data,index=['k','Ya','v','s'])
print(s0)
print("---------------------------------")

#Eaxmple 3 -Dict:


d1={'a':0.1,'b':90.77,'c':78.9,'d':02.99}
s2=pd.Series(d1)
print(s2)


print("____________")



#example4-emp id and name
empdata={101:'koti',1092:'ramu',102:"somu",103:"ghj"}
s3=pd.Series(empdata)
print(s3)
print("__________")

#example5- customzied indexes by using index()
pdata={"a":78,'b':67,'c':90,'d':93}
s4=pd.Series(pdata,index=['b','c','d','a'])
print(s4)

print("-----------")

#Creation of scalar value to series
s5=pd.Series(7,index=[10,11,21,31,41,61])#7 is constant value for series DS
print(s5)
print("________")

dl={'s':10,'j':20,'c':56,'d':34}
ser2=pd.Series(dl,index=['s','n2','n3','n4'])
print(ser2)#key value printed in the place of s and remaining will be printed as NAN
print("________1")
print(pd.Series(dl,index=['n1','n2','c','n4']))
print("________")
#print(ser2[0])

#Acesssing data from series with Position

hj=pd.Series([10,20,30,40,50])
print(hj[:2])
print('\n')
print(hj[-3:])

print(type(hj))












