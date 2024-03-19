from SDES_EXAMPLE_sdes import *

IV='00000000'
key10='1010000010'
text="TTT One Nine Two"

def enc(key10, text, IV ):
    marray=bArray(text)
    C=[]
    
    lxr=logical_xor(marray[0], IV)
    C.append(E(key10,lxr))
    for j in range(1,len(marray),1):
        lxr=logical_xor(C[j-1],marray[j])
        c=E(key10,lxr)
        C.append(c)
    print('C' , C)
    text = ''
    for i in C:
        o = int(i,2)
        text+=chr(o)
    return text



def dec(key10, text, IV):
    cc = bArray(text)
    de = []
    lxr = logical_xor(D(key10, cc[0]), IV)
    de.append(lxr)
    for j in range(1, len(cc), 1):
        xD = D(key10, cc[j])
        y1 = cc[j-1]
        lxr = logical_xor(xD, y1)
        de.append(lxr)
    text = ''.join([chr(int(block, 2)) for block in de])

    return text

b = enc(key10, text, IV)
a = dec(key10, b, IV)

print(b)
print('dec', a)