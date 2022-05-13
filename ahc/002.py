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
passed = [False] * num
dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]
def dfs(pr_h, pr_w):
    passed[t[pr_h][pr_w]] = True
    for i in range(4):
        nx_h, nx_w = pr_h + dh[i], pr_w + dw[i]
        if 0 <= nx_h < num and 0 <= nx_w < num\
            and passed[t[nx_h][nx_w]]:
            return
    return
dfs(si, sj)
