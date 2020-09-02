
def minDivisor(n):
    i = 2
    while i < (n**(1/2) + 1):
        if n % i == 0:
            return i
        i += 1
    return n

def minDivisorFor(n):
    for i in range(2, n**(1/2) + 1):
        if n % i == 0:
            return i
    return n


n = int(input())
print(minDivisor(n))
