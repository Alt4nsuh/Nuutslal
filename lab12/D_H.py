import sys
sys.path.append("C:\\A_Hicheel\\Python\\Ugugdul_nuuh")
from lab3.ds import PrimitiveRoot
from lab3.lab3 import miller_rabin
def primitive_check(a,q):
    b=-1
    for i in range(len(q)):
      if q[i] == a:
        b=1
        break
    return b
def calcK(Y,X,q):
  K=pow(Y,X,q)
  return K
while 1:
    q = int(input("Enter P : "))
    if miller_rabin(q) == False:
        print("Number Is Not Prime, Please Enter Again!")
        continue
    break

b=PrimitiveRoot(q)
while 1:
    a = int(input(f"Choose The Primitive Root Of {b} : "))
    if primitive_check(a, b) == -1:
        print(f"Number Is Not A Primitive Root Of {q}, Please Try Again!")
        continue
    break
  

while 1:
    Xa, Xb = int(input("Enter The Private Key Of User Alice : ")), int(
    input("Enter The Private Key Of User Bob: "))
    if Xa >= q or Xb >= q:
        print(f"Private Key Of Both The Users Should Be Less Than {q}!")
        continue
    break

Ya=pow(a,Xa,q)
Yb=pow(a,Xb,q)


print(f"Alice: {calcK(Yb,Xa,q)}")
print(f"Bob: {calcK(Ya,Xb,q)}")




# Xd1=11
# Xd2=7

# Yd1=pow(a,Xd1,q)
# Yd2=pow(a,Xd2,q)
# print(f"Middle Alice: {calcK(Ya,Xd2,q)}")
# print(f"Middle Bob: {calcK(Yb,Xd1,q)}")