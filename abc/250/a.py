# input
h, w = [int(_) for _ in input().split()]
r, c = [int(_) for _ in input().split()]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0
for i in range(4):
    x = r + dx[i]
    y = c + dy[i]
    if 0 < x <= h and 0 < y <= w and abs(r - x) + abs(c - y) == 1:
        ans += 1
print(ans)