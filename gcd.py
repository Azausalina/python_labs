def GCD(A, B):
    if B != 0:
        C = A % B
        A = GCD(B, C)
    return A


A = int(input())
B = int(input())
print(GCD(A, B))
