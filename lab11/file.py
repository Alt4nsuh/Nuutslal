import sys
sys.path.append('C:/A_Hicheel/Python/Ugugdul_nuuh/lab11')
import mod
import numpy as np

abc = 'abcdefghijklmnopqrstuvwxyz'
abc += abc.upper()
abc += '0123456789 !@#?$'

print("Alphabet:", abc)

st = 'How are you?'

lst = [abc.index(chr) for chr in st]
print("Indexes:", lst)

arr = np.array(lst).reshape(-1, 2)
print("Reshaped array:", arr)

P = [i[0] * 100 + i[1] for i in arr]
print("Converted integers:", P)

C = []  # Encrypted message
P1 = []  # Decrypted message

p = 73
q = 151
n = p * q
e = 11
et = (p - 1) * (q - 1)
d = pow(e, -1, et)

def RSA(P, p, q, qw):
    C = []
    P1 = []
    n = p * q
    e = 11
    et = (p - 1) * (q - 1)
    d = pow(e, -1, et)
    
    if qw == "en":
        for pp in P:
            C.append(mod.myPow(e, pp, n))
    elif qw == "de":
        for cc in P:
            pp = mod.myPow(d, cc, n)
            P1.append(pp)
            x1 = pp // 100
            x2 = pp % 100
            C.append(x1)
            C.append(x2)
    
    return C 

C = RSA(P, p, q, "en")
D = RSA(C, p, q, "de")

# Convert decrypted message into characters
decrypted_message = ''.join([abc[ind] for ind in D])
print("Decrypted message:", decrypted_message)

# Display encrypted and decrypted messages
print("Encrypted message:", C)
print("Decrypted message:", D)
