def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])   # path compression
        return par[x]

def are_same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

# input
n, q = [int(i) for i in input().split()]
p, a, b = [], [], []
for _ in range(q):
    x, y, z = [int(i) for i in input().split()]
    p.append(x); a.append(y); b.append(z)

par, rank = [0] * n, [0] * n

for i in range(n):
    par[i] = i

for i in range(q):
    if p[i]:
        if are_same(a[i], b[i]):
            print("Yes")
        else:
            print("No")
    else:
        unite(a[i], b[i])
