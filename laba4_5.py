def dist(x1, y1, x2, y2):
    k1 = abs(x1 - x2)
    k2 = abs(y1 - y2)
    return (k1**2 + k2**2)**(1/2)


def isPointInCircle(x, y, xc, yc, r):
    return dist(x, y, xc, yc) <= r


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
print("YES" if isPointInCircle(a, b, c, d, e) else "NO")
