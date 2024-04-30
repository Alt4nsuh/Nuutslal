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
        dtd=dtd//gcd
        dtu=dtu//gcd
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
        dtd=dtd//gcd
        dtu=dtu//gcd
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
    return P
abc = "abcdefghijklmnopqrstuvwxyz"
abc += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abc += "012345678 "
ecc_alp = [(5, 246),(126, 107),(188, 226),(56, 248),(4, 46),(221, 63),(156, 137),
           (63, 53),(163, 251),(233, 43),(53, 29),(68, 84),(164, 7),(49, 14),(86, 157),
           (80, 56),(177, 35),(159, 127),(210, 1),(229, 114),(185, 13),(39, 132),
           (99, 67),(178, 198),(42, 117),(153, 110),(197, 90),(125, 156),(143, 91),
           (240, 123),(94, 124),(253, 73),(192, 19),(29, 235),(249, 189),(55, 141),
           (226, 70),(168, 122),(15, 162),(136, 128),(30, 221),(0, 32),(223, 229),
           (254, 45),(3, 58),(47, 48),(90, 245),(201, 164),(100, 254),(20, 172),(137, 8),
           (93, 171),(113, 159),(75, 205),(122, 41),(34, 39),(200, 10),(217, 62),
           (82, 149),(203, 178),(193, 121),(60, 87)]
def encrypt(message, G, k, a, p):
    Pm = message
    c1 = mult(k, G, a, p)
    c2 = ECC_PQ(Pm, mult(k, Pb, a, p), a, p)
    return c1, c2

def decrypt(ciphertext, nb, a, p):
    c1, c2 = ciphertext
    Mp = ECC_PQ(c2, esreg(mult(nb, c1, a, p)), a, p)
    return Mp
pText="hello "
ecc_text=[]


p=257;a=0;b=-4
G=(2,2)
nb1=101
V= DT()
ecc_dec=[]
Pb=mult(nb1,G,a,p)
kk=[0,1,4,5,7,8,10,11,14,16,17,20,22,23,25,26,28,29,31,32,34,35,37,38,40,41,44,46,49,52,53,55,56,58,59,61,62,64,65,67,68,70,71,73,74,76,77,80,83,85,88,89,91,92,94,95,97,98,100,101,103,104,106,107,109,112,113,115,118,119,121,122,124,125,128,]
# for k in range(p):
#  try:
#     for i in pText:
#         ind = abc.index(i)
#         ecc_abc =  ecc_alp[ind]
#         ecc_text.append(ecc_abc)
#         c1 = mult(k, G, a, p)
#         c2 = ECC_PQ(ecc_abc, mult(nb1, Pb, a, p), a, p)
#         Mr=ECC_PQ(c2,esreg(mult(nb1,c1,a,p)),a,p)
#     #print(k,end=",")
#  except:
#      ss=1
for i in pText:
        ind = abc.index(i)
        ecc_abc =  ecc_alp[ind]
        ecc_text.append(ecc_abc)
for i in ecc_text:
  Pm=i
  V = rndAES(V)
  kk1=int(V,16)%75
  k=kk[kk1]
  c1,c2=encrypt(i, G, k, a, p)
  ecc_dec.append((c1,c2))
print(ecc_dec)
decre=""
for i in ecc_dec:
    de=decrypt(i, nb1, a, p)
    ind=ecc_alp.index(de)
    decre +=(abc[ind])
print("",decre)
