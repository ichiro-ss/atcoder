# input
n = int(input())
a = [int(_) for _ in input().split()]

ans = 0
for v in a:
    if v > 10:
        ans += v - 10
print(ans)