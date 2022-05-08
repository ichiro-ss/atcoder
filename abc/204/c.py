import sys
sys.setrecursionlimit(10 ** 6)
# input
n, m = [int(_) for _ in input().split()]
g = [[] for _ in range(n)]
for i in range(m):
    a, b = [int(_) - 1 for _ in input().split()]
    g[a].append(b)

def dfs(cur):
    if passed[cur]:
        return
    passed[cur] = True
    for nx in g[cur]:
        dfs(nx)

ans = 0
for i in range(n):
    passed = [False for _ in range(n)]
    dfs(i)
    ans += sum(passed)
print(ans)