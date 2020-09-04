def phib(n, p=0, c=0):
    if p == 0 and c == 0:
        c = 1
    if n - 1 > 0:
        c = phib(n-1, c, c+p)
    return c


n = int(input())
print(phib(n))
