from SDES_EXAMPLE_sdes import *

text="TTT One Nine Two"
key10='1010000010'
#CN* = PN* ⊕ MSBu[E(K, TN)]
def CNT_enc(text,key10):
    marray=bArray(text)
    C=""
    n=0
    for p in marray:
        nt=decimalToBinary(n,8)
        O=E(key10,nt)
        lxr=logical_xor(p,O)
        ch = int (lxr,2)
        a=chr(ch)
        C+=(a)
        n+=1
    return C


cText =CNT_enc(text , key10)
print('Counter enc ',cText)
print('Counter dec',CNT_enc(cText,key10))

