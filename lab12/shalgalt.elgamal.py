
import sys
sys.path.append("C:\\A_Hicheel\\Python\\Ugugdul_nuuh\\lab2")
from lab2 import egcd,ET,prime_factors
from lab2 import PrimitiveRoot
sys.path.append("C:\\A_Hicheel\\Python\\Ugugdul_nuuh")
from lab9.aes import DT
from lab9.aes import rndAES
sys.path.append("C:\\A_Hicheel\\Python\\Ugugdul_nuuh")
from lab11.mod import myPow
def modinv(a,m):
    g,x,y= egcd(a,m)
    if g !=1:
        raise Exception('Error')
    else:
        return x%m
def en_elgamal(st,q,a,Ya):

    en=[]
    for ch in st:
        M = 14
        k=7
        K = myPow(Ya, k, q)
        C1 = myPow(a, k, q)
        C2 = (M * K) % q
        en.append (C1)
        en.append (C2)
    return en

def de_elgamal(ss,Xa,q):
    de = []
    for i in range(0,len(ss),2):
        C1=(17)
        C2=(20)
        K=myPow(C1,Xa,q)
        k_1 = modinv(K,q)
        m=(C2*k_1)%q
        de.append (m)
    return de

q=31
a = 3
Xa = 10
Ya = 25
 
st ="L"
print("__________________",st)
en = en_elgamal(st,q,a,Ya)

print(en)

de = de_elgamal(en,Xa,q)
print(de)
abc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"

print(abc[de[0]])