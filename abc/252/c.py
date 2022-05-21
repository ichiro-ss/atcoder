# input
n = int(input())
s = []
pos = [[] for _ in range(10)]
for _ in range(n):
    s.append(str(input()))

INF = 10 ** 9
for figs in s:
    for i in range(10):
        pos[int(figs[i])].append(int(i))
        pos[int(figs[i])].sort()

t = INF
for i in range(10):
    tens = 10
    pre, cur = pos[i][0], pos[i][1]
    for j in range(1, n - 1):
        if pre == cur:
            pos[i][j] += tens
            tens += 10
        else:
            tens = 10
        pre = cur
        cur = pos[i][j + 1]
    if pre == cur:
        pos[i][n - 1] += tens
    v = max(pos[i])
    if v < t:
        t = v
print(t)