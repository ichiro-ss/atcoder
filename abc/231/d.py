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

# input here
n, m = [int(_) for _ in input().split()]
a, b = [0] * m, [0] * m
for i in range(m):
    a[i], b[i] = [int(_) - 1 for _ in input().split()]

cnts = [0] * n
uf = UnionFind(n)
ans = "Yes"
for i in range(m):
    if uf.are_same(a[i], b[i]):
        ans = "No"
        break
    else:
        uf.unite(a[i], b[i])
    cnts[a[i]] += 1
    cnts[b[i]] += 1

for i in range(n):
    if cnts[i] > 2:
        ans = "No"
        break
print(ans)