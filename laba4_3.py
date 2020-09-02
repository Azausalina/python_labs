def dist(x1, y1, x2, y2):
    k1 = abs(x1 - x2)
    k2 = abs(y1 - y2)
    return (k1**2 + k2**2)**(1/2)


def p_3angle(x1, y1, x2, y2, x3, y3):
    d1 = dist(x1, y1, x2, y2)
    d2 = dist(x1, y1, x3, y3)
    d3 = dist(x3, y3, x2, y2)
    return d1 + d2 + d3


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
print(p_3angle(a, b, c, d, e, f))
