import sys
sys.path.append('C:/A_Hicheel/Python/Ugugdul_nuuh/lab11') 
import mod

import numpy as np
abc='abcdefghijklmnopqrstuvwxyz'
abc+=abc.upper()
abc+='0123456789 !@#?$'
print(abc)
st='How are you?'

lst=[]
P=[]

for chr in st:
    lst.append(abc.index(chr))
print(lst)

arr = np.array(lst).reshape(-1,2)
print(arr)
for i in arr:
    st2=i[0]*100+i[1]
    P.append(st2)
print(P)
C=[]
P1=[]
p=73; q=151; n=p*q; e=11; et=(p-1)*(q-1); d=pow(e,-1,et)
print("asa",d)
lst1=[]
def RSA(P,p,q):
    n=p*q; e=11; et=(p-1)*(q-1)
    for pp in P:
        C.append(mod.myPow(e,pp,n))
    for cc in P:
      pp=mod.myPow(d,cc,n)
      P1.append(pp)
      x1=pp//100;x2=pp%100
      lst1.append(x1);lst1.append(x2)
    return C
C= RSA(P,p,q)
for cc in C:
    pp=mod.myPow(d,cc,n)
    P1.append(pp)
    x1=pp//100;x2=pp%100
    lst1.append(x1);lst1.append(x2)
strnew=''
print(lst1)

for ind in lst1:
  print(abc[ind])
  strnew+=abc[ind]
  
print("list1",lst1)
print("p1",P1)
print(strnew)