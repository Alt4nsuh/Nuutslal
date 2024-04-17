import numpy as np
from mod import myPow

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#?$'
print(abc)
st = 'How are you?'
print([abc.index(c) for c in st])  

lst = [abc.index(c) for c in st]

if len(lst) % 2 != 0:
    lst.append(0) 
arr = np.array(lst).reshape(-1, 2)
print(arr)
P = [x[0] * 100 + x[1] for x in arr]
print(P)

p = 73
q = 151
n = p * q
e = 11
et = (p - 1) * (q - 1)
d = pow(e, -1, et)
print("Decryption key (d):", d)

C = [myPow(x, e, n) for x in P]
print("Encrypted:", C)

decrypted_indices = [myPow(x, d, n) for x in C]
print("Decrypted indices:", decrypted_indices)

decrypted_message = []
for index in decrypted_indices:
    high = index // 100
    low = index % 100
    if high < len(abc): decrypted_message.append(abc[high])
    if low < len(abc): decrypted_message.append(abc[low])

strnew = ''.join(decrypted_message)
print("Decrypted message:", strnew)
