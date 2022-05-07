# input
n, k = [int(_) for _ in input().split()]
a = []
for i in range(n):
    a.append([int(_) for _ in input().split()])

sa = sorted(a)
for i in range(n):
    if sa[i][0] > k:
        break
    k += sa[i][1]
print(k)