import bisect
# input
n, q = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
x = []
for _ in range(q):
    x.append(int(input()))

a.sort()

for i in range(q):
    print(n - bisect.bisect_left(a, x[i]))
