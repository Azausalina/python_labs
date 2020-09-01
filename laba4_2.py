def dist(x1, y1, x2, y2):
    k1 = abs(x1 - x2)
    k2 = abs(y1 - y2)
    return (k1**2 + k2**2)**(1/2)

a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(dist(x1 = a, y1 = b, x2 = c, y2 = d))
