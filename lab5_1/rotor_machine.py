def rotn(n):
    l=[]
    k=0
    for i in range(0,26):
        k=(n+i)%26+1
        l.append(k)
    return l
abc="abcdefghijklmnopqrstuvwxyz"
r1=[21,3,15,1,19,10,14,26,20,8,16,7,22,4,11,5,17,9,12,23,18,2,25,6,24,13]
r2=[20,1,6,4,15,3,14,12,23,5,16,2,22,19,11,18,25,24,13,7,10,8,21,9,26,17]
r3=[8,18,26,17,20,22,10,3,13,11,4,23,5,24,9,12,25,16,19,6,15,21,2,7,1,14]
r11=rotn(23)
r21=rotn(25)
r31=rotn(0)
def rotM(rl11):
    rl11=rl11[::-1]
    temp=rl11[0]
    rl11=rl11[1:26]
    rl11.append(temp)
    rl11=rl11[::-1]
    return rl11
def rotorM(r11,r1):
    r11=rotM(r11)
    r1=rotM(r1)
    return r11,r1
def fnd(r1,r2,in1,n):
    x1=r1[(in1-n)%26]
    out1=r2.index(x1)
    return out1


def rotor_en(x1):
    out=""
    for x in x1:
        up="abcdefghijklmnopqrstuvwxyz"
        in1=up.index(x)
        in1=fnd(r11,r1,in1,1)+1
        in1=fnd(r21,r2,in1,0)
        in1=fnd(r31,r3,in1,0)
        out+=abc[in1]
    return out


def rotor_de(x1):
    out=""
    for x in x1:
        up="abcdefghijklmnopqrstuvwxyz"
        in1=up.index(x)
        in1=fnd(r3,r31,in1,0)
        in1=fnd(r2,r21,in1,0)
        in1=(fnd(r1,r11,in1,1)+1)%26
        out+=up[in1]
    return out


x1='hi'
x1=rotor_en(x1)
print(x1)
x1=rotor_de(x1)
print(x1)



