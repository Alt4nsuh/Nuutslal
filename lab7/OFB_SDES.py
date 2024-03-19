from SDES_EXAMPLE_sdes import *

text="TTT One Nine Two"
key10='1010000010'

nonce='00000000'
def OFB_enc(text, key10, nonce):
    marray=bArray(text)
    C=""
    #CN* = PN* ⊕ MSBu(ON)
    for p in marray:
        O=E(key10,nonce)
        lxr=logical_xor(p,O)
        ch=int(lxr,2)
        a= chr(ch)
        nonce=O
        C+=(a)
    return C
cText = OFB_enc(text,key10,nonce)
print('OFB',OFB_enc(text,key10,nonce))
print('OFB',OFB_enc(cText,key10,nonce))
