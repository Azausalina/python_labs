def isPrime(n):
    if n == 2:
        return "YES"
    i = 2
    while i < (n**(1/2) + 1):
        if n % i == 0:
            return "NO"
        i += 1
    return "YES"


print(isPrime(int(input())))
