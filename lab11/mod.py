def myPow(a, e, n):
    
    f = 1
    for bit in bin(e)[2:]:
        f = (f * f) % n
        if bit == '1':
            f = (f * a) % n

    return f
