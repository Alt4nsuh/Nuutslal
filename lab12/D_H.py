import random as rnd

def primitiveRoot(p):
  prt=[]

  for a in range(2,p):
      for i in range(1,p):
          pr=pow(a,i,p)
          if pr==1:
              break
      if i==p-1:
          print(a,end=" ")

  return prt
a=primitiveRoot(257)

q = 257; a=a[10]

Xa = 51
Ya = pow(a,Xa,q)

st = 'Hello elgamal cipher'

for ch in st:
    M = ord(ch)
    k = rnd.randrange(q)
    K=pow(Ya,k,q)
    C1=pow(a,k,q)
    C2=(M*K)%q
    print(C1,',',C2,end=',')