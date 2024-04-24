import sys
sys.path.append("C:\\A_Hicheel\\Python\\Ugugdul_nuuh")
from lab9.aes import DT
from lab9.aes import rndAES
def GCD(x, y): 
    if y!=0: 
        x=GCD(y,x%y) 
    return x

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
  




    
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&()*+,-./\:;<=>?@[\]^_`{|}~\n\t'

ecc_alp =[(22, 12), (5, 246), (126, 107), (188, 226), (56, 248), (4, 46), (221, 63), (156, 137), (63, 53), (163, 251), (233, 43), (53, 29), (68, 84), (164, 7), (49, 14), (86, 157), (80, 56), (177, 35), (159, 127), (210, 1), (229, 114), (185, 13), (39, 132), (99, 67), (178, 198), (42, 117), (153, 110), (197, 90), (125, 156), (143, 91), (240, 123), (94, 124), (253, 73), (192, 19), (29, 235), (249, 189), (55, 141), (226, 70), (168, 122), (15, 162), (136, 128), (30, 221), (0, 32), (223, 229), (254, 45), (3, 58), (47, 48), (90, 245), (201, 164), (100, 254), (20, 172), (137, 8), (93, 171), (113, 159), (75, 205), (122, 41), (34, 39), (200, 10), (217, 62), (82, 149), (203, 178), (193, 121), (60, 87), (51, 99), (51, 158), (60, 170), (193, 136), (203, 79), (82, 108), (217, 195), (200, 247), (34, 218), (122, 216), (75, 52), (113, 98), (93, 86), (137, 249), (20, 85), (100, 3), (201, 93), (90, 12), (47, 209), (3, 199), (254, 212), (223, 28), (0, 225), (30, 36), (136, 129), (15, 95), (168, 135), (226, 187), (55, 116), (249, 68), (29, 22), (192, 238), (253, 184), (94, 133)]

def encrypt(message, G, k, a, p):
    Pm = message
    c1 = mult(k, G, a, p)
    c2 = ECC_PQ(Pm, mult(k, Pb, a, p), a, p)
    return c1, c2

def decrypt(ciphertext, nb, a, p):
    c1, c2 = ciphertext
    Mp = ECC_PQ(c2, esreg(mult(nb, c1, a, p)), a, p)
    return Mp
pText="Hello world"
ecc_text=[]
for i in pText:
  ind = abc.index(i)
  ecc_abc =  ecc_alp[ind]
  ecc_text.append(ecc_abc)

p=257;a=0;b=-4
G=(2,2)
nb=101
Pb=mult(nb,G,a,p)
V= DT()
for i in ecc_text:
  Pm=i
  V = rndAES(V)
  k=int(V,16)%p
  print("k=",k)
  c1,c2=encrypt(i, G, k, a, p)
  print(f"c1={c1} c2={c2}")
# Pb=multss(nb,G,a,p)
# print(Pb)

# c1=multss(k,G,a,p)
# c2=ECC_PQ(Pm,multss(k,Pb,a,p),a,p)

# print(f"c1={c1} c2={c2}")


# Mp=ECC_PQ(c2,esreg(multss(nb,c1,a,p)),a,p)

# print('MP=',Mp)