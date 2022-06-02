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
sum_v = 0

def nway(x):
    return (x + 2 if x + 2 < 4 else x - 2)

def calc_dfs(past_dir, pr_h, pr_w, passed, tht):
    global sum_v
    passed[pr_h][pr_w] = True
    sum_v += 1
    num = str(format(tht[pr_h][pr_w], '04b'))
    pr_dir = []
    for i in range(len(num)):
        if num[i] == '1' and i != nway(past_dir):
            pr_dir.append(i)
    print(pr_dir)
    for i in pr_dir:
        nx_h, nx_w = pr_h + dh[i], pr_w + dw[i]
        if 0 <= nx_h < n and 0 <= nx_w < n:
            if str(format(tht[nx_h][nx_w], '04b'))[nway(i)] == '1':    # means those are connected
                if passed[nx_h][nx_w]:  # means a cycle
                    print("this is closed")
                    sum_v = 0
                    return
                else:
                    calc_dfs(i, nx_h, nx_w, passed, tht)

    return

# def calc_score(tht):
#     max_s = 0
#     passed = [[False for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if passed[i][j]:
#                 continue
#             num = str(format(tht[i][j], '04b'))
#             pr_dir = []
#             for k in range(len(num)):
#                 if num[k] == '1':
#                     pr_dir.append(k)

#             passed[i][j] = True
#             for d in pr_dir:
#                 nx_i, nx_j = i + dh[d], j + dw[d]
#                 if 0 <= nx_i < n and 0 <= nx_j < n:
#                     score = calc_dfs(d, nx_i, nx_j, passed, 0, tht)
#                     if max_s < score:
#                         max_s = score
#             # print(passed)
#     return max_s

# print(calc_score(t))
passed = [[False for _ in range(n)] for _ in range(n)]
calc_dfs(-4, 3, 5, passed, t)
print(sum_v)