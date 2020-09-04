def GCD(A, B):
    if B != 0:
        C = A % B
        A = GCD(B, C)
    return A


def reduceFraction(pair):
    k = GCD(*pair)
    return pair[0] // k, pair[1] // k


pair = int(input()), int(input())
print(*reduceFraction(pair))
