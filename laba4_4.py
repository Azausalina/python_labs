def min_max(coord, edge1=-1, edge2=1):
    return (coord >= edge1) and (coord <= edge2)


def isPointInSquare(x, y):
    return min_max(x) and min_max(y)


x = float(input())
y = float(input())
print("YES" if isPointInSquare(x, y) else "NO")
