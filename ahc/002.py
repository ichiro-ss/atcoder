import sys
sys.setrecursionlimit(10 ** 9)
num = 50
# input
si, sj = [int(_) for _ in input().split()]
t, p = [], []
for _ in range(num):
    t.append([int(_) for _ in input().split()])
for _ in range(num):
    p.append([int(_) for _ in input().split()])

# solution1 print null string (4861 points)
# print()

# solution2 simple dfs
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
dir = ["U", "D", "L", "R"]

ans_way = ""
max_score = 0
def dfs(pr_h, pr_w, so_far, score, passed):
    global max_score, ans_way

    passed[t[pr_h][pr_w]] = True
    for i in range(4):
        nx_h, nx_w = pr_h + dh[i], pr_w + dw[i]
        if 0 <= nx_h < num and 0 <= nx_w < num and not passed[t[nx_h][nx_w]]:
            nx_score = score + p[nx_h][nx_w]
            nx_way= so_far + dir[i]
            dfs(nx_h, nx_w, nx_way, nx_score, passed)

    if score > max_score:
        max_score = score
        ans_way = so_far

dfs(si, sj, "", p[si][sj], [False] * (num * num))
print(ans_way)
