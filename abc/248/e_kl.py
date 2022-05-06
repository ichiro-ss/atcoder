from math import gcd
# input
n, k = [int(i) for i in input().split()]
x, y = [0]*n, [0]*n
for i in range(n):
    x[i], y[i] = [int(j) for j in input().split()]

params = {}
if n == 1 or k == 1:
    print("Infinity")
    exit()
for i in range(n):
    for j in range(i):
        a, b = x[i] - x[j], y[i] - y[j]
        if a < 0:
            a, b = -a, -b
        if a == 0:
            b = 1
        else:
            g = gcd(a, b)
            a //= g; b //= g
        c = a * y[i] - b * x[i]
        if (a, b, c) not in params:
            params[(a, b, c)] = 1
        else:
            params[(a, b, c)] += 1
ans = 0
for p in params:
    if params[p] >= k * (k - 1) // 2:
        ans += 1
print(ans)

