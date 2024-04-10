def myPow(b,a,n):
  f=1
  c=0
  for bi in bin(b)[2:]:
    c=c*2
    f=(f*f)%n
    if bi == "1":
      c=c+1
      f=(f*a)%n
  return f