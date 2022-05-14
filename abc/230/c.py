# input
n, a, b = [int(_) for _ in input().split()]
p, q, r, s = [int(_) for _ in input().split()]

grids = [["." for _ in range(s - r + 1)] for _ in range(q - p + 1)]

h = max(p - a, r - b)
w = min(q - a, s - b)
for i in range(h, w + 1):
    grids[a + i - p][b + i - r] = "#"

h = max(p - a, b - s)
w = min(q - a, b - r)
for i in range(h, w + 1):
    grids[a + i - p][b - i - r] = "#"

for i in range(q - p + 1):
    for j in range(s - r + 1):
        print(grids[i][j], end = "")
    print()
