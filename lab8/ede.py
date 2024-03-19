import datetime as dt
import sys
sys.path.append(r'C:\A_Hicheel\Python\Ugugdul_nuuh') 
from lab7.SDES_EXAMPLE_sdes import *
def EDE(K1,K2,P):
  return E(K1,D(K2,E(K1,P)))
def fZfil(t,n):
    s = bin(t)[2:]
    s=s[::-1] #inverse hiij bga         1011 bsn bol 11010000 bolood
    s=s+"0"*(n-len(s))
    s=s[::-1]                             #ene deer 00001011 bolno
    return s

def XOR(a,b):
    aa = int(a,2)
    bb = int(b,2)
    cc = aa^bb
    T=fZfil(cc,8)
    return T

def DT():
    dt1 = dt.datetime.now()
    t = str(dt1)
    t=t[-6:]
    t = int(t,10)%256
    T=fZfil(t,8)
    return T
IV = fZfil(3,8)
K1='1010000010'
K2='1010000011'


def x9(K1,K2,IV):
  dti=DT()
  ede1=EDE(K1,K2,dti)
  xor=XOR(ede1,IV)
  R=EDE(K1,K2,xor) #ede2
  xor2=XOR(ede1,R)
  IV=EDE(K1,K2,xor2)
  return R,IV

for i in range(10):
  R,IV=x9(K1,K2,IV)
  print(R,int(R,2))
  