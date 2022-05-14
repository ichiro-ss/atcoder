# input
n, d = [int(_) for _ in input().split()]
walls = []
for _ in range(n):
    walls.append([int(_) for _ in input().split()])

walls.sort(reverse=False, key = lambda x: x[1])
ans = 0
idx = -(10 ** 9 + 1)
for l, r in walls:
    if idx + d - 1 < l:
        ans += 1
        idx = r
print(ans)