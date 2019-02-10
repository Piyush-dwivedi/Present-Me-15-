import pandas as pd
import numpy as np
data=pd.read_csv(r'C:\present me\pr.csv')
data2=pd.read_csv(r'C:\present me\Attendance\Attendance_2019-02-10_13-17-40.csv')
x=data.iloc[:, 0].values
y=data2.iloc[:, 0].values
z=data.iloc[:,-1].values
cleaned=[x for x in z if str(x)!='nan']
cleaned2=[x for x in x if str(x)!='nan']
z=data
n=len(cleaned2)
k=y.size
List1=[]
List2=[]
List4=[]
list5=[]
for i in range (0,n):
    List1.append(cleaned2[i])
    List4.append(cleaned[i])
for j in range (0,k):
    List2.append(y[j])
list3=[]
j=0
for i in List1:
    if i not in List2:
        list3.append(i)
        list5.append(List4[j])
    j=j+1

raw_data={'id':list3,'no':list5}
df=pd.DataFrame(raw_data,columns=['id','no'])
df.to_csv('pro.csv',index='False')
df_new=pd.read_csv('pro.csv').drop(['Unnamed: 0'],axis=1)
df_new.to_csv('file2.csv',index='False')