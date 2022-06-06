# this is my score calculator of ahc011
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

def calc_dfs(past_dir, pr_h, pr_w, passed, sum_v, tht):
    num = str(format(tht[pr_h][pr_w], '04b'))
    print(pr_h, pr_w)
    pr_dir = []
    is_back = False
    for i in range(len(num)):
        if num[i] == '1':
            if i == nway(past_dir):
                is_back = True
            else:
                pr_dir.append(i)
    # if pr_h == 0 and pr_w == 1:
    #     print(is_back, pr_dir)
    if is_back:
        if passed[pr_h][pr_w]:  # means closed
            print(pr_h, pr_w, pr_dir, past_dir, num)
            return -1
        else:
            for i in pr_dir:
                passed[pr_h][pr_w] = True
                if sum_v < 0:
                    break
                sum_v += 1
                nx_h, nx_w = pr_h + dh[i], pr_w + dw[i]
                if 0 <= nx_h < n and 0 <= nx_w < n:
                    calc_dfs(i, nx_h, nx_w, passed, sum_v, tht)
    else:
        passed[pr_h + dh[nway(past_dir)]][pr_w + dw[nway(past_dir)]] = True
    return sum_v

def calc_score(tht):
    max_s = 0
    passed = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if passed[i][j]:
                continue
            num = str(format(tht[i][j], '04b'))
            pr_dir = []
            for k in range(len(num)):
                if num[k] == '1':
                    pr_dir.append(k)

            passed[i][j] = True
            for d in pr_dir:
                nx_i, nx_j = i + dh[d], j + dw[d]
                if 0 <= nx_i < n and 0 <= nx_j < n:
                    score = calc_dfs(d, nx_i, nx_j, passed, 0, tht)
                    if max_s < score:
                        max_s = score
            print(i, j, score)
            # print(passed)
    return max_s

print(calc_score(t))

# I added score_now() which search a empty grid and a moved grid
# and return the max tree length of them