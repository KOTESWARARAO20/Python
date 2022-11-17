import pandas as pd
# Calling DataFrame constructor
df=pd.DataFrame()#by using pandas alias name calling dataframe ds or corresponding datastructure
print(df)
print(type(df))
#list input dataframe
l=['sun','mon','wen','tue','fri','sat','san']
df1=pd.DataFrame(l)
print(df1)
#ex2:
data=[['ROS',10],['popy',12],['sunny',14]]
df=pd.DataFrame(data,columns=['Name','Age'])
print(df)#instead of 1 dim we are provide the  2 dim
print("----------------------")
#ex3:
d1={'Name':['tom','sam','jerry','steve'],'Age':[28,34,29,42]}
print(pd.DataFrame(d1))
print("________")

#ex4:Indexed dataframe using arrays
d3={'Name':['sam','peter','john','mary'],'Age':[20,40,50,60]}

df2=pd.DataFrame(d3,index=['rk1','rk2','rk3','rk4'])
print(df2)
print("________")


#ex5:Create a dataframe from list of dicts:
#instead of passing single dict,list of dict,2 dict given to DF
d4=[{'a':30,'b':50},{'a':50,'b':106,'c':210}]
# Calling DataFrame constructor on list
df3=pd.DataFrame(d4)
print(df3)
print("________")
print("Describe Method")
print(df3.describe())

#Create df by passing list of dicts and row indices


