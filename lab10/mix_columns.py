import sys
sys.path.append('C:/A_Hicheel/Python/Ugugdul_nuuh/lab9/') 
import aes  
def gmul(a, b):
        p = 0
        for c in range(8):
            if b & 1:
                p ^= a
            a <<= 1
            if a & 0x100:
                a ^= 0x11b
            b >>= 1
        return p
def decimalToBinary(n,b):
  bnr = bin(n).replace("0b","")
  bnr=bnr.rjust(b,"0")
  return bnr
def mix_columns(st):
    ss = []
    st2=[]
    for i in range(0,4):
        ss.append(st[i*4:i*4+4])
    print(ss)
    for i in range(0,4):
        gg=0
        gg^=gmul(0x02,ss[i][0])
        print(f"02* {st_w_16(ss[i][0])} = {decimalToBinary(gmul(0x02,ss[i][0]),8)}")
        gg^=gmul(0x03,ss[i][1])
        print(f"03 * {st_w_16(ss[i][1])} = {decimalToBinary(gmul(0x02,ss[i][1]),8)}")
        gg^=ss[i][2]
        print(f"{ss[i][2]} = {decimalToBinary(ss[i][2],8)}")
        gg^=ss[i][3]
        print(f"{ss[i][3]} = {decimalToBinary(ss[i][3],8)}")
        st2.append(gg)
        print("-------------------------------------")
        print(gg,'=',bin(gg)[2:],"\n",)
        
        gg=0
        gg^=ss[i][0]
        print(f"{st_w_16(ss[i][0])} = {decimalToBinary(ss[i][0],8)}")
        gg^=gmul(0x02,ss[i][1])
        print(f"02 * {st_w_16(ss[i][1])} = {decimalToBinary(gmul(0x02,ss[i][1]),8)}")
        gg^=gmul(0x03,ss[i][2])
        print(f"03 * {st_w_16(ss[i][2])} = {decimalToBinary(gmul(0x02,ss[i][2]),8)}")
        gg^=ss[i][3]
        print(f"{st_w_16(ss[i][3])} = {decimalToBinary(ss[i][3],8)}")
        st2.append(gg)
        print("-------------------------------------")
        print(gg,'=',bin(gg)[2:],"\n",)
        gg=0
        gg^=ss[i][0]
        print(f"{st_w_16(ss[i][0])} = {decimalToBinary(ss[i][0],8)}")
        gg^=ss[i][1]
        print(f"{st_w_16(ss[i][1])} = {decimalToBinary(ss[i][1],8)}")
        gg^=gmul(0x02,ss[i][2])
        print(f"02 * {st_w_16(ss[i][2])} = {decimalToBinary(gmul(0x02,ss[i][2]),8)}")
        gg^=gmul(0x03,ss[i][3])
        print(f"03 * {st_w_16(ss[i][3])} = {decimalToBinary(gmul(0x02,ss[i][3]),8)}")
        st2.append(gg)
        print("-------------------------------------")
        print(gg,'=',bin(gg)[2:],"\n",)

        gg=0
        gg^=gmul(0x03,ss[i][0])
        print(f"03 * {st_w_16(ss[i][0])} = {decimalToBinary(gmul(0x02,ss[i][0]),8)}")
        
        gg^=ss[i][1]
        print(f"{st_w_16(ss[i][1])} = {decimalToBinary(ss[i][1],8)}")
        
        gg^=ss[i][2]
        print(f"{st_w_16(ss[i][2])} = {decimalToBinary(ss[i][2],8)}")

        gg^=gmul(0x02,ss[i][3])
        print(f"02 * {st_w_16(ss[i][3])} = {decimalToBinary(gmul(0x02,ss[i][3]),8)}")
        print("-------------------------------------")        
        print(gg,'=',bin(gg)[2:],"\n",)

        st2.append(gg)
                 
    return st2
    ss = []
    st2=[]
    for i in range(0,4):
        ss.append(st[i*4:i*4+4])
    print(ss)
    for i in range(0,4):
        gg=0
        gg^=gmul(0x02,ss[i][0])
        print(f"02* {st_w_16(ss[i][0])} = {decimalToBinary(gg,8)}")
        gg^=gmul(0x03,ss[i][1])
        print(f"03 * {st_w_16(ss[i][1])} = {decimalToBinary(gg,8)}")
        gg^=ss[i][2]
        print(f"{gg} = {decimalToBinary(gg,8)}")
        gg^=ss[i][3]
        print(f"{gg} = {decimalToBinary(gg,8)}")
        st2.append(gg)
        print("-------------------------------------")
        gg=0
        gg^=ss[i][0]
        print(f"{st_w_16(ss[i][0])} = {decimalToBinary(ss[i][0],8)}")
        gg^=gmul(0x02,ss[i][1])
        print(f"02 * {st_w_16(ss[i][1])} = {decimalToBinary(gg,8)}")
        gg^=gmul(0x03,ss[i][2])
        print(f"03 * {st_w_16(ss[i][2])} = {decimalToBinary(gg,8)}")
        gg^=ss[i][3]
        print(f"{st_w_16(ss[i][3])} = {decimalToBinary(ss[i][3],8)}")
        
        st2.append(gg)

        gg=0
        gg^=ss[i][0]
        print(f"{st_w_16(ss[i][0])} = {decimalToBinary(ss[i][0],8)}")
        gg^=ss[i][1]
        print(f"{st_w_16(ss[i][1])} = {decimalToBinary(ss[i][1],8)}")
        gg^=gmul(0x02,ss[i][2])
        print(f"02 * {st_w_16(ss[i][2])} = {decimalToBinary(gg,8)}")
        gg^=gmul(0x03,ss[i][3])
        print(f"03 * {st_w_16(ss[i][3])} = {decimalToBinary(gg,8)}")
        st2.append(gg)

        gg=0
        gg^=gmul(0x03,ss[i][0])
        print(f"03 * {st_w_16(ss[i][0])} = {decimalToBinary(gg,8)}")
        
        gg^=ss[i][1]
        print(f"{st_w_16(ss[i][1])} = {decimalToBinary(ss[i][1],8)}")
        
        gg^=ss[i][2]
        print(f"{st_w_16(ss[i][2])} = {decimalToBinary(ss[i][2],8)}")

        gg^=gmul(0x02,ss[i][3])
        print(f"02 * {st_w_16(ss[i][3])} = {decimalToBinary(gg,8)}")
        
        st2.append(gg)
                 
    return st2
def st_W_16(w):
  hex_w = ""

  for word in w:
        hex_word = ''.join(format(word, '02x') )
        hex_w+=hex_word
  return     hex_w 
def st_w_16(w):
        hex_word = ''.join(format(w, '02x') )
        return hex_word
with open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab10/realText.txt", "r") as file1:
    realText = file1.read()
realText_list = aes.st_2_16(realText)

result = mix_columns(realText_list)
a=st_W_16(result)
with open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab10/mix_columns.txt", "w") as file2:
    file2.write(a)
