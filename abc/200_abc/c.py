# input
n = int(input())
a = [int(i) for i in input().split()]

mods = [0 for i in range(200)]
for i in range(n):
    mods[(a[i] % 200)] += 1
ans = 0
for i in range(200):
    num = mods[i]
    if num > 1:
        ans += int(num * (num - 1) / 2)

print(ans)