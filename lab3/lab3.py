#1. Miller Rabin test код бич. Зарим үр дүнг хавсаргах
import sys
sys.path.append("C:\\A_Hicheel\\Python\\Ugugdul_nuuh\\lab2")
from lab2 import prime_factors
from math import gcd
import random
def miller_rabin(n):
 if n == 2:
  return True
 if n % 2 == 0:
  return False
 if n % 3 == 0:
  return False
 k ,q = 0, n - 1
 while q % 2 == 0:
   k += 1
   q //= 2   
   a = random.randrange(2, n - 1)
   x = pow(a, q, n)
 if x == 1 or x == n - 1:
   return True
 for _ in range(k - 1):
   x = pow(x, 2, n)
 if x == n - 1:
  return True
 return False

def root(a):
  for c in range(1,a,1):
    if gcd(c,a)==1:
      bb.append(c)
  return bb      
def EulerFunction(N):
 if miller_rabin(N[0]):
  return (N[0]-1)*N[0]**(N[1]-1)
a = 10
bb=[]



# print(a," toonii prime factor ",prime_factors(a))
# print("Tsuvaa",root(a))

# for b in prime_factors(a):
#   if(miller_rabin(b[0])):
#    print(b[0],"prime number mun")
 
     