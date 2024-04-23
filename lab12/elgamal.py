
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
    V=DT()
    en=""
    for ch in st:
        M = ord(ch)
        V = rndAES(V)
        k=int(V,16)%q
        K = myPow(Ya, k, q)
        C1 = myPow(a, k, q)
        C2 = (M * K) % q
        en += chr(C1)
        en += chr(C2)
    return en

def de_elgamal(ss,Xa,q):
    de = ""
    for i in range(0,len(ss),2):
        C1=(ord(ss[i]))
        C2=(ord(ss[i+1]))
        K=myPow(C1,Xa,q)
        k_1 = modinv(K,q)
        m=(C2*k_1)%q
        de += chr(m)
    return de

q=257
a = 101
Xa = 51
Ya = myPow(a, Xa, q)




file1 = open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab12/file.txt", "r") 
st = file1.read()
file1.close() 
print("__________________",st)
en = en_elgamal(st,q,a,Ya)
file1 = open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab12/e_file.txt", "w", encoding="utf-8")
 
file1.write(en)
file1.close() 
file1 = open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab12/e_file.txt", "r" ,encoding="utf-8") 
st = file1.read()
file1.close() 
de = de_elgamal(en,Xa,q)
file1 = open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab12/d_file.txt", "w", encoding="utf-8")
file1.write(de)
file1.close()