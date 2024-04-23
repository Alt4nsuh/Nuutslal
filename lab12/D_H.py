import sys
sys.path.append("C:\\A_Hicheel\\Python\\Ugugdul_nuuh\\lab3")
from lab3 import lab3
print(lab3.miller_rabin(3))
a=3
q=353
Xa=97
Xb=233
Xd1=12
Xd2=24

Yd1=pow(a,Xd1,q)
Yd2=pow(a,Xd2,q)

Ya=pow(a,Xa,q)

Yb=pow(a,Xb,q)
def calcK(Y,X,q):
  K=pow(Y,X,q)
  return K

print(f"Alice: {calcK(Yd2,Xa,q)}")
print(f"Bob: {calcK(Yd1,Xb,q)}")
print(f"Middle Alice: {calcK(Ya,Xd2,q)}")
print(f"Middle Bob: {calcK(Yb,Xd1,q)}")