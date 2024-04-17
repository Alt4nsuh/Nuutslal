import sys
sys.path.append('C:/A_Hicheel/Python/Ugugdul_nuuh/lab11')
import mod
import numpy as np

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&()*+,-./\:;<=>?@[\]^_`{|}~\n\t'

file1 = open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab11/file.txt", "r") 
st = file1.read()
file1.close() 
if len(st)%2 == 1 :
    st = st + " "
lst = [abc.index(chr) for chr in st]

arr = np.array(lst).reshape(-1, 2)
# print("Reshaped array:", lst)

P = [i[0] * 100 + i[1] for i in arr]

p = 73
q = 151
n = p * q
e = 11
et = (p - 1) * (q - 1)
d = pow(e, -1, et)

def RSA(P, p, q, qw):
    C = []
    n = p * q
    e = 11
    et = (p - 1) * (q - 1)
    d = pow(e, -1, et)
    
    if qw == "en":
        for pp in P:
            C.append(mod.myPow(pp, e, n))
    elif qw == "de":
        for cc in P:
            pp = mod.myPow(cc, d, n)
            x1 = pp // 100
            x2 = pp % 100
            C.append(x1)
            C.append(x2)
    
    return C 
def f_to_t(C):
    B = []
    for cc in C:
            x1 = cc // 100
            x2 = cc % 100
            B.append(hex(x1)[2:])
            B.append(hex(x2)[2:])
    return B
C = RSA(P, p, q, "en")
# print(C)
E=f_to_t(C)
# print("EEEEE",E)
e_message = ''.join([ind for ind in E ])
# print("Encrypted message:", e_message)
file1 = open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab11/e_file.txt", "w") 
file1.write(e_message)
file1.close() 
D = RSA(C, p, q, "de")
# print("D",D)
decrypted_message = ''.join([abc[ind] for ind in D if ind < len(abc)])
# print("Decrypted message:", decrypted_message)
file1 = open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab11/d_file.txt", "w") 
file1.write(decrypted_message)
file1.close()