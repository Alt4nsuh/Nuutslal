import math  

def gcd(x, y):
    while y:
        print(x, y)
        x, y = y, x % y
    return x

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = gcdExtended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
    return gcd, x, y

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, y, x = egcd(b % a, a)
        return (gcd,x-(b//a)*y,y)

def prime_factors(n):
    pf = []
    tt = 0
    while n % 2 == 0:
        n = n // 2
        tt += 1
    if tt != 0:
        pf.append([2, tt])
    tt = 0
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            tt += 1
        if tt != 0:
            pf.append([i, tt])
        tt = 0
    if n > 2:
        pf.append([n, 1])
    return pf

def el(pp):
    return pow(pp[0], pp[1] - 1) * (pp[0] - 1)

def ET(f1):
    f = 1
    for pp in f1:
        f*=el(pp)
    return f

def PrimitiveRoot(num, et):
    if num == 1:
        return [0]
    if num == 2:
        return [1]
    root = []
    for i in range(2, num):
        if gcd(i, num) == 1:
            for j in range(1, et):
                if (i**j % num == 1) and (j != et):
                    break
            if (i**j % num == 1) and (j == et):
                root.append(i)
                break
    return root
