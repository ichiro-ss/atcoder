from termios import CINTR


n, k = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
sa = sorted(a)

by_k = k
for i in range(k):
    idx = i
    b = []
    while idx < n:
        b.append(a[idx])
        idx += k
    b.sort()

    for j in range(len(b)):
        if b[j] != sa[i + (k * j)]:
            print("No")
            exit()
print("Yes")
