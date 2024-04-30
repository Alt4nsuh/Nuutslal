a = 7
c = 0
m = 32
X0 = 1

# Calculate X1
X1 = (7 * X0) % m

# Calculate X2
X2 = (7 * X1) % m
X3 = (7 * X2) % m
X4 = (7 * X3) % m
X5 = (7 * X4) % m

print("X2 =", X5)
print(pow(-11,1,7))