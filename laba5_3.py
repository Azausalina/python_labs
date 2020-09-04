
n = int(input())

flag1 = "+___ "
flag2 = "|{} / ".format(1)
flag3 = "|__\ "
flag4 = "|    "

for i in range(2, n+1):
    flag1 += "+___ "
    flag2 += "|{} / ".format(i)
    flag3 += "|__\ "
    flag4 += "|    "

print(flag1, flag2, flag3, flag4, sep="\n")
