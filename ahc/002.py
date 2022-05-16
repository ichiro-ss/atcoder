import time
from random import shuffle
import sys
st = time.time()
sys.setrecursionlimit(10 ** 9)
num = 50

# input
si, sj = [int(_) for _ in input().split()]
t = [[int(_) for _ in input().split()] for _ in range(num)]
p = [[int(_) for _ in input().split()] for _ in range(num)]

# solution3 dfs till end
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
dir = ["U", "D", "L", "R"]

ans_way = ""
max_score = 0
def dfs(pr_h, pr_w, so_far, score, passed):
    global max_score, ans_way, st

    if (time.time() - st) > 1.8:
        if score > max_score:
            max_score = score
            ans_way = so_far
        return

    passed[t[pr_h][pr_w]] = True
    idxs = list(range(4))
    shuffle(idxs)
    for i in idxs:
        nx_h, nx_w = pr_h + dh[i], pr_w + dw[i]
        if 0 <= nx_h < num and 0 <= nx_w < num and not passed[t[nx_h][nx_w]]:
            nx_score = score + p[nx_h][nx_w]
            nx_way= so_far + dir[i]
            dfs(nx_h, nx_w, nx_way, nx_score, passed)

    if score > max_score:
        max_score = score
        ans_way = so_far

while True:
    dfs(si, sj, "", p[si][sj], [False] * (num * num))
    if (time.time() - st) > 1.8:
        break
print(ans_way)
