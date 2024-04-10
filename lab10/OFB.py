import sys
sys.path.append('C:/A_Hicheel/Python/Ugugdul_nuuh/lab9/') 
import aes 
Key = "cfb0ef3108d49cc4562d5810b0a9af60"

with open("C:/A_Hicheel/Python/Ugugdul_nuuh/lab10/ofb.txt", "r") as f:
    V = f.read()

for i in range(8):
    V = aes.AES(Key, V)
    print(V)