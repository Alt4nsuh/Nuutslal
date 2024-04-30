import sys
sys.path.append("C:\\A_Hicheel\\Python\\Ugugdul_nuuh")
from lab9.aes import DT
from lab9.aes import rndAES
def GCD(x, y): 
    if y != 0: 
        print(f"{x} = {x//y} * {y} + {x%y}")
        x = GCD(y, x % y)
    return x

# Example usage
print(GCD(24140, 40902))

def mood(dtu,dtd):
    gcd=GCD(dtu,dtd)
    if gcd==dtd:
        dt=dtu//dtd
    else:
        dtd=(dtd//gcd)%p
        dtu=(dtu//gcd)%p
        dt=(pow(dtd,-1,p)*dtu)%p
    return dt
def PQ(P,Q,p):
    xQ=Q[0];yQ=Q[1]
    xP=P[0];yP=P[1]

    dtu=(yQ-yP)%p
    dtd=(xQ-xP)%p

    gcd=GCD(dtu,dtd)
    if gcd==dtd:
        dt=dtu//dtd
    else:
        dtd=(dtd//gcd)%p
        dtu=(dtu//gcd)%p
        dt=(pow(dtd,-1,p)*dtu)%p
            
    return dt



def PP(P,a,p):
    xP=P[0];yP=P[1]
    dtu=(3*(xP**2)+a)%p
    dtd=(2*yP)%p
    
    gcd=GCD(dtu,dtd)
    if gcd==dtd:
        dt=dtu//dtd
    else:
        dtd=(dtd//gcd)%p
        dtu=(dtu//gcd)%p
        dt=(pow(dtd,-1,p)*dtu)%p
            
    return dt
def ECC_PQ(P,Q,a,p):
    if P[0]==Q[0] and P[1]==Q[1]:
        L=PP(P,a,p)
    else:
        L=PQ(P,Q,p)
        
    xQ=Q[0];yQ=Q[1]
    xP=P[0];yP=P[1]
    
    xR = (L**2 - xP - xQ) % p
    yR = (L*(xP - xR) - yP) % p
    return (xR,yR)
def esreg(PP):
  return(PP[0],-PP[1])
def mult(na,G,a,p):
    P=G
    
    for i in range(1,na):
       P=ECC_PQ(P,G,a,p)
       #print(i,P,end=', ')
    return P
def encrypt(message, G, k, a, p):
    Pm = message
    c1 = mult(k, G, a, p)
    c2 = ECC_PQ(Pm, mult(k, Pb, a, p), a, p)
    return c1, c2

def decrypt(ciphertext, nb, a, p):
    c1, c2 = ciphertext
    Mp = ECC_PQ(c2, esreg(mult(nb, c1, a, p)), a, p)
    return Mp
p=23;a=9;b=17
G=(16,5)
nb=101
for i in range(1,10):
  Pb=mult(i,G,a,p)
  print(f"{i}-{Pb}")
  
print(PP((3,10),1,p))  
print(PQ((3,10),(9,7),p))  
  
  

# Pb=multss(nb,G,a,p)
# print(Pb)

# c1=multss(k,G,a,p)
# c2=ECC_PQ(Pm,multss(k,Pb,a,p),a,p)

# print(f"c1={c1} c2={c2}")


# Mp=ECC_PQ(c2,esreg(multss(nb,c1,a,p)),a,p)

# print('MP=',Mp)