import random


def vernam(realText,K):
    outText=""
    up="abcdefghijklmnopqrstuvwxyz"
    up+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    up+="0123456789 "
    
    v=[]
    i=0
    for eachLetter in realText:
        P = up.index(eachLetter)
        ki=up.index(K[i])
        C = P ^ ki
        v.append(C)
        i+=1
    return v
def vernamd(Text,K):
    outTxt=""
    
    up="abcdefghijklmnopqrstuvwxyz"
    up+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    up+="0123456789 "
    
    for i in range(len(Text)):
        P=Text[i]
        indk=up.index(K[i])
        PT = P ^ indk
        outTxt+=up[PT]
        
    return outTxt
realText="hello"
key="YM2ybjD1EpsqgH57FJfn86LQxk4VRAKlBWSodZI39PaucXNCmTzrv0GiOtwheU "
outText=""
outText=vernam(realText,key)
print(outText)
ppText=vernamd(outText,key)

print(ppText)














