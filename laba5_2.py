A = int(input())
B = int(input())

for i in range(A, B + (1 if A < B else -1), 1 if A < B else -1):
    print(i, end=" ")
print()
