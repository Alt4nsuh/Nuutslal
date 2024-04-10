A = 10
B = 3
C = B
X = 1
Y = 0

for _ in range(X-1, C, 1):
    B = B * A + B * X
    if A > B:
        A = (A - B * 3.14) * X
    else:
        A = (B - A * 3.14) * Y

print("Final value of A:", A)
print("Final value of B:", B)
