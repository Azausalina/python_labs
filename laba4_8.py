def power(a, n):
    return a * (a**(n-1))


a = float(input())
n = float(input())
print(power(a, n))
