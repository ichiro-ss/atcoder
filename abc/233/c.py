import sys
sys.setrecursionlimit(10 ** 9)

# input
n, x = [int(_) for _ in input().split()]
l, a = [], []
for _ in range(n):
    array = [int(_) for _ in input().split()]
    l.append(array[0])
    a.append(array[1:])

ans = 0
def dfs(bag, product):
    global ans
    if bag == n:
        if product == x:
            ans += 1
        return
    for v in a[bag]:
        if product * v > x:
            continue
        dfs(bag + 1, product * v)

dfs(0, 1)
print(ans)