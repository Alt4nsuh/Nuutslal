INIT_BITS = 128
def leftRotation(n,d):
    return ((n << d) | (n >> (INIT_BITS - d))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

def rightRotation(n,d):
    return (n >> d) |(n << (INIT_BITS - d)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

s = 'test above functions'; hh=[]

st='88515907'
def h(st):
    myHash=0; myHash1=0;st1=""
    for ch in st:
        nt=ord(ch)
        st1=st1+hex(nt)[2:]
    for i in range(0,len(st1),32):
        hh.append(int(st1[i:i+32],32))

    for hhh in hh:
        myHash=rightRotation(myHash,1)^hhh
        myHash1=myHash1^hhh
    return myHash

print("myHash: ", hex(h(st+s))[2:])