# input
n = int(input())
a = [int(_)-1 for _ in input().split()]
b = [int(_)-1 for _ in input().split()]
c = [int(_)-1 for _ in input().split()]

idxs = {}
for i in range(len(c)):
    if c[i] not in idxs:
        idxs[c[i]] = 1
    else:
        idxs[c[i]] += 1

bcnt = {}
for k, v in idxs.items():
    if b[k] not in bcnt:
        bcnt[b[k]] = v
    else:
        bcnt[b[k]] += v

ans = 0
for i in range(n):
    if a[i] in bcnt:
        ans += bcnt[a[i]]
print(ans)