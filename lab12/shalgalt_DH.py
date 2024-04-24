import sys
sys.path.append("C:\\A_Hicheel\\Python\\Ugugdul_nuuh")
from lab3.ds import PrimitiveRoot
from lab3.lab3 import miller_rabin

def primitive_check(a, q):
    b = -1
    for i in range(len(q)):
        if q[i] == a:
            b = 1
            break
    return b

def calcK(Y, X, q):
    K = pow(Y, X, q)
    return K

def calcY(a, X, q):
    Y = pow(a, X, q)
    return Y

def find_x(a, q, Y):
    x = 0
    while x<q:
        result = pow(a, x, q)
        if result == Y:
            return x
        x += 1

q = 71
a = 7

Y = 9

X=5


YY=calcY(a, X, q)
XX=find_x(a, q, Y)
print(f"Y = {YY}") 
print("X =", XX)  
K= calcK(Y, X, q)
print(K)
