# input
n, w = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

a.sort()
ans = 0
figs = set()

for i in range(n):
    if a[i] not in figs and a[i] <= w:
        figs.add(a[i])
        ans += 1

for i in range(n):
    for j in range(i+1, n):
        fig = a[i] + a[j]
        if fig not in figs and fig <= w:
            figs.add(fig)
            ans += 1

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            fig = a[i] + a[j] + a[k]
            if fig not in figs and fig <= w:
                figs.add(fig)
                ans += 1
print(ans)