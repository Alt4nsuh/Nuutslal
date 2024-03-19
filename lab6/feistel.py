def decimalToBinary(n,b):
  bnr = bin(n).replace("0b","")
  bnr=bnr.rjust(b,"0")
  return bnr
def binArray(text):
  binF=[]
  for i in text:
    p=decimalToBinary(ord(i),8)
    binF.append(p[0:4])  
    binF.append(p[4:])  
  return binF
def enc(plaintext):
  tx=""
  print(binArray(plaintext))
  for i in binArray(plaintext):
   pt=int(i,2)
   en = f_ed[pt]
   tx += (hex(en)[2:])
  return tx
def dec(plaintext):
    tx = ""
    hex_values = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]
    for hex_val in hex_values:
        pt1 = int(hex_val[0], 16)
        pt2 = int(hex_val[1], 16)
        de1 = f_ed.index(pt1)
        de2 = f_ed.index(pt2)
        tmdgt = de1 * 16 + de2
        tx += chr(tmdgt)
    return tx


f_ed=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
plaintext="helloo"

print(enc(plaintext))
print(dec(enc(plaintext)))