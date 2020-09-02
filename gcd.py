def GCD(A, B):
    if B != 0:
        C = A % B
        A = GCD(B, C)
    return A

A = 36
B = 48

print(GCD(A, B))