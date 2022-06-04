from random import randrange
import copy
import time
st = time.time()
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
    best_h, best_w = 0, 0
    passed = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # sum_v = 0
            if passed[i][j]:
                continue
            # num = str(format(tht[i][j], '04b'))
            # pr_dir = []
            # for k in range(len(num)):
            #     if num[k] == '1':
            #         pr_dir.append(k)

            val = calc_dfs(-4, i, j, passed, tht, 0)
            if max_s < val:
                max_s = val
                best_h, best_w = i, j
    return max_s, best_h, best_w

def score_now(y1, x1, y2, x2, tht, max_sc, best_h, best_w):
    # (x1, y1) means a empty grid, (x2, y2) means a moved grid

    passed = [[False for _ in range(n)] for _ in range(n)]
    num = str(format(tht[y2][x2], '04b'))
    for i in range(len(num)):
        if num[i] == '1':
            if 0 <= y1+dh[i] < n and 0 <= x1+dw[i] < n:
                sc = calc_dfs(-4, y1+dh[i], x1+dw[i], passed, tht, 0)
                if max_sc < sc:
                    max_sc = sc
                    best_h, best_w = y1+dh[i], x1+dw[i]
    
    for i in range(4):
        if num[i] == '1':
            if 0 <= y2+dh[i] < n and 0 <= x2+dw[i] < n:
                sc = calc_dfs(-4, y2+dh[i], x2+dw[i], passed, tht, 0)
                if max_sc < sc:
                    max_sc = sc
                    best_h, best_w = y2+dh[i], x2+dw[i]

    return max_sc, best_h, best_w


all_max_idx, all_max_v, all_ans_way = 0, 0, ""
while True:
    ch_t = copy.deepcopy(t)
    if time.time() - st > 2.7:
        break
    max_v, best_h, best_w = calc_score(t)
    max_idx, ans_way = 0, ""
    pr_h, pr_w = sh, sw
    pre_dir = -4
    i = 0
    while len(ans_way) < T:
        if time.time() - st > 2.7:
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
            sc, best_h, best_w = score_now(nx_h, nx_w, pr_h, pr_w, ch_t, max_v, best_h, best_w)
            if max_v < sc:
                max_idx, max_v = i, sc
            pr_h, pr_w = nx_h, nx_w
            pre_dir = idx
    if all_max_v < max_v or (all_max_v == max_v and all_max_idx > max_idx):
        all_max_idx, all_max_v = max_idx, max_v
        all_ans_way = ans_way[:all_max_idx]
    
print(all_ans_way)

