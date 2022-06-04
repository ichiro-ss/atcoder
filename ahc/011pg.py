# from random import shuffle
from random import randrange
import copy
# import sys
import time
st = time.time()
# sys.setrecursionlimit(10 ** 9)
# input
n, T = [int(_) for _ in input().split()]
t = [[int(_, base = 16) for _ in list(input())] for _ in range(n)]

# find a empty grid
sh, sw = 0, 0
for i in range(n):
    for j in range(n):
        if t[i][j] == 0:
            sh, sw = i, j

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]
dir = ["D", "R", "U", "L"]

ans_way = ""
max_score = 0

def nway(x):
    return (x + 2 if x + 2 < 4 else x - 2)

def calc_dfs(past_dir, pr_h, pr_w, passed, tht, sum_v):
    passed[pr_h][pr_w] = True
    sum_v += 1
    num = str(format(tht[pr_h][pr_w], '04b'))
    pr_dir = []
    for i in range(len(num)):
        if num[i] == '1' and i != nway(past_dir):
            pr_dir.append(i)
    # print(pr_dir)
    for i in pr_dir:
        nx_h, nx_w = pr_h + dh[i], pr_w + dw[i]
        if 0 <= nx_h < n and 0 <= nx_w < n:
            if str(format(tht[nx_h][nx_w], '04b'))[nway(i)] == '1':    # means those are connected
                if passed[nx_h][nx_w]:  # means a cycle
                    sum_v = -110
                    return sum_v
                else:
                    sum_v = calc_dfs(i, nx_h, nx_w, passed, tht, sum_v)
    return sum_v

def calc_score(tht):
    max_s = 0
    passed = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum_v = 0
            if passed[i][j]:
                continue
            num = str(format(tht[i][j], '04b'))
            pr_dir = []
            for k in range(len(num)):
                if num[k] == '1':
                    pr_dir.append(k)

            val = calc_dfs(-4, i, j, passed, tht, 0)
            if max_s < val:
                max_s = val
            # print(passed)
    return max_s

# swap t[y1][x1] and t[y2][x2]
def swap(y1, x1, y2, x2, tht):
    tmp = tht[y1][x1]
    tht[y1][x1] = t[y2][x2]
    tht[y2][x2] = tmp
    return tht

# move the empty grid
# def solve_dfs(past_dir, pr_h, pr_w, so_far, score, tht):
#     global max_score, ans_way, st

#     if max_score < score:
#         max_score, ans_way = score, so_far
#         print(ans_way)

#     if (time.time() - st) > 1.3:
#         return

#     if len(ans_way) >= 10:
#         return
    
#     idxs = list(range(4))
#     shuffle(idxs)
#     for i in idxs:
#         if i == nway(past_dir):
#             continue
#         nx_h, nx_w = pr_h + dh[i], pr_w + dw[i]
        
#         if 0 <= nx_h < n and 0 <= nx_w < n:
#             nx_t = swap(pr_h, pr_w, nx_h, nx_w, tht)
#             nx_score = calc_score(nx_t)
#             nx_way = so_far + dir[i]
#             solve_dfs(i, nx_h, nx_w, nx_way, nx_score, nx_t)
    
#     if score > max_score:
#         max_score = score
#         ans_way = so_far
#     return

# LIMIT = min(4 * n * n, T)
all_max_idx, all_max_v, all_ans_way = 0, 0, ""
while True:
    ch_t = copy.deepcopy(t)
    if time.time() - st > 2.85:
        break
    max_idx, max_v, ans_way = 0, 0, ""
    pr_h, pr_w = sh, sw
    pre_dir = -4
    i = 0
    while len(ans_way) < T:
        if time.time() - st > 2.85:
            break
        idx = randrange(4)
        if idx == nway(pre_dir):
            continue
        nx_h, nx_w = pr_h + dh[idx], pr_w + dw[idx]

        if 0 <= nx_h < n and 0 <= nx_w < n:
            tmp = ch_t[pr_h][pr_w]
            ch_t[pr_h][pr_w] = ch_t[nx_h][nx_w]
            ch_t[nx_h][nx_w] = tmp

            i+= 1
            ans_way = ans_way + dir[idx]
            sc = calc_score(ch_t)
            if max_v < sc:
                max_idx, max_v = i, sc
            pr_h, pr_w = nx_h, nx_w
            pre_dir = idx
    if all_max_v < max_v or (all_max_v == max_v and all_max_idx > max_idx):
        all_max_idx, all_max_v = max_idx, max_v
        all_ans_way = ans_way[:all_max_idx]
    
print(all_ans_way)

# print(calc_score(t))
# solve_dfs(-4, sh, sw, "", 0, t)
# print(ans_way)
# print(max_score)
