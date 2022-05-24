# input
n, m = [int(_) for _ in input().split()]
s = [str(_) for _ in input().split()]
t = [str(_) for _ in input().split()]

ex = 0
for i in range(n):
    if s[i] == t[ex]:
        print("Yes")
        ex += 1
    else:
        print("No")