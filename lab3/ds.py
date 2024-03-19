from lab2.lab2 import gcdExtended
from lab2.lab2 import gcd 

def EulerTotientList(num):
    lst = []
    for i in range(1, num):
        if gcd(i, num) == 1:
            lst.append(i)
    return lst

def EulerTotientPrime(num, pow):
    if not MillerRabin(num):
        return None
    return (num-1) * num**(pow-1)

def MillerRabin(n):
    if n <= 1:
        return None
    if n in {2, 7, 61}:
        return True
    elif n % 2 == 0:
        return False

    littleNum = [2, 7, 61]
    bigNum = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    def Check(a):
        x = pow(a, d, n)
        if x in {1, n - 1}:
            return True
        for _ in range(s - 1):
            x = pow(x, 2, n)
        if x == n - 1:
            return True
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    if n < 2**32:
        res = True
        for i in littleNum:
            if not Check(i):
                res = False
                break
        return res

    res = True
    for i in bigNum:
        if not Check(i):
            res = False
            break
    return res

def PrimitiveRoot(num):
    if num == 1:
        return [0]
    if num == 2:
        return [1]
    eu = gcdExtended(num)
    root = []
    for i in range(2, num):
        if gcd(i, num) == 1:
            for j in range(1, eu):
                if (i**j % num == 1) and (j != eu):
                    break
            if (i**j % num == 1) and (j == eu):
                root.append(i)
                break
    return root

primes = [i for i in range(2, 100) if MillerRabin(i)]
print(primes)
print(PrimitiveRoot(27))
print(EulerTotientPrime(7, 2))
print(EulerTotientList(35))
