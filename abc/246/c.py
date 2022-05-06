n, k, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

for i in range(n):
    if a[i] >= x and k > 0:
        cnt = a[i] // x
        a[i] -= (min(cnt, k) * x)
        k -= min(cnt, k)
    if k == 0:
        break
list.sort(a, reverse = True)
i = 0
while k and i < n:
    a[i] = 0
    i += 1
    k -= 1
print(sum(a))