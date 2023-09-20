from collections import deque

INF = int(1e9)

# input
h, w = [int(i) for i in input().split()]
c = []
for i in range(h):
    c.append([str(j) for j in list(input())])

# search for the start and the goal
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = j, i
        if c[i][j] == "g":
            gx, gy = j, i
            
d = [[INF for _ in range(w)] for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# def dfs_recursion(que):
#     if not len(que):
#         print(d[gy][gx])
#         return d[gy][gx]
#         exit()
#     p = que.pop()
#     if p[0] == gy and p[1] == gx:
#         return d[gy][gx]
#         exit()
#     for i in range(4):
#         ny = p[0] + dx[i]
#         nx = p[1] + dy[i]
#         if 0 <= nx < w and 0 <= ny < h and c[ny][nx] != "#"\
#         and d[ny][nx] == INF:
#             que.append([ny, nx])
#             d[ny][nx] = d[p[0]][p[1]] + 1
#     dfs_recursion(que)
    
# def dfs_r():
#     que = deque()
#     que.append([sy, sx])
#     d[sy][sx] = 0
#     return dfs_recursion(que)

def dfs():
    que = deque()
    que.append([sy, sx])
    d[sy][sx] = 0

    while len(que):
        p = que.pop()
        if p[0] == gy and p[1] == gx:
            break
        for i in range(4):
            ny = p[0] + dx[i]
            nx = p[1] + dy[i]
            if 0 <= nx < w and 0 <= ny < h and c[ny][nx] != "#"\
            and d[ny][nx] == INF:
                que.append([ny, nx])
                d[ny][nx] = d[p[0]][p[1]] + 1
    return d[gy][gx]

res = dfs()
# for i in range(h):
    # print(d[i])
if res != INF:
    print("Yes")
else:
    print("No")