import copy
import sys
sys.setrecursionlimit(10 ** 9)
class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def are_same(self, x, y):
        return self.root(x) == self.root(y)



# input
f = [int(_) for _ in input().split()]

len_row = 10
box = [[0 for i in range(len_row)] for j in range(len_row)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move_r(b):
    for i in range(len_row):
        figs = []
        for j in range(len_row):
            if b[i][j]:
                figs.append(b[i][j])
        b[i] = [0]*(len_row-len(figs)) + figs
    return b

def move_l(b):
    for i in range(len_row):
        figs = []
        for j in range(len_row):
            if b[i][j]:
                figs.append(b[i][j])
        b[i] = figs + [0]*(len_row-len(figs))
    return b

def move_u(b):
    for i in range(len_row):
        figs = []
        for j in range(len_row):
            if b[j][i]:
                figs.append(b[j][i])
        for k in range(len_row):
            if k < len(figs):
                b[k][i] = figs[k]
            else:
                b[k][i] = 0
    return b

def move_b(b):
    for i in range(len_row):
        figs = []
        for j in range(len_row):
            if b[j][i]:
                figs.append(b[j][i])
        for k in range(len_row):
            if k < 10-len(figs):
                b[k][i] = 0
            else:
                b[k][i] = figs[len(figs)+k-10]
    return b

def calc_score(b):
    uf = UnionFind(len_row*len_row)
    #passed = [[False for i in range(len_row)] for j in range(len_row)]
    for i in range(len_row):
        for j in range(len_row):
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if 0 <= ni < len_row and \
                    0 <= nj < len_row:
                    if b[i][j] == b[ni][nj]:
                        uf.unite(i*10 + j, ni*10 + nj)
    cnt = [0 for i in range(len_row*len_row)]
    for i in range(len_row):
        for j in range(len_row):
            if uf.par[i*10 + j]>=0:
                cnt[uf.par[i*10 + j]] += 1
    sc = 0
    # for i in range(10):
    #     print(uf.par[i*10:i*10+10])
    # idxs = [i for i in range(len_row*len_row)]
    # for i in range(len_row):
    #     for j in range(len_row):
    #         for k in range(len(dx)):
    #             ni, nj = i + dy[k], j + dx[k]
    #             if 0 <= ni < len_row and \
    #                 0 <= nj < len_row:
    #                 if b[i][j] == b[ni][nj]:
    #                     idxs[ni*10 + nj] = idxs[i*10 + j]
    # cnt = [0 for i in range(len_row*len_row)]
    # for i in range(len_row):
    #     for j in range(len_row):
    #         if b[i][j]:
    #             cnt[i*10 + j] += 1
    # for i in range(len_row):
    #     print(idxs[i*10:i*10+10])
    # print()
    # sc = 0

    for i in range(len_row):
        for j in range(len_row):
            if cnt[i*10 + j] > 0 and b[i][j] > 0:
                sc += cnt[i*10 + j] + 1
    return sc

for _ in range(len_row*len_row):
    place = int(input())
    idx = 0
    for i in range(len_row):
        for j in range(len_row):
            if not box[i][j]:
                idx += 1
            if idx == place:
                box[i][j] = f[_]
                break
        if idx == place:
            break

    d = [0]*4

    r = move_r(copy.deepcopy(box))
    d[0] = calc_score(r)
    l = move_l(copy.deepcopy(box))
    d[1] = calc_score(l)
    b = move_b(copy.deepcopy(box))
    d[2] = calc_score(b)
    u = move_u(copy.deepcopy(box))
    d[3] = calc_score(u)

    max_idx = d.index(max(d))
    # print(d)
    if max_idx == 0:
        print("R")
        box = move_r(box)
    elif max_idx == 1:
        print("L")
        box = move_l(box)
    elif max_idx == 2:
        print("B")
        box = move_b(box)
    else:
        print("F")
        box = move_u(box)
    # print(max(d))
    # for i in range(len_row):
    #     print(box[i])

