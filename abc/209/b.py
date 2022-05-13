# input
n, x = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

for i in range(n):
    if i % 2:
        x -= (a[i] - 1)
    else:
        x -= a[i]
if x < 0:
    print("No")
else:
    print("Yes")