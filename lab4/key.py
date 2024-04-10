def keyTable(alp,key):
  key1= "".join(sorted(set(key), key=key.index))
  alp1=alp
  for el in key1:
    alp1=alp1.replace(el,"")
  ppr=key1+alp1
  for i in range(25):
    if i!=0 and i%5==0:
      print()
    print(ppr[i],end=" ")
  print(len(ppr))
alp ="GRAVITYFLSBCDEHKMNOPQUWXZ"
key="monarchy"

keyTable(alp,key)
