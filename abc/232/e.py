# input
h, w, k = [int(_) for _ in input().split()]
x1, y1, x2, y2 = [int(_) for _ in input().split()]

num = 998244353
dp = [[0 for _ in range(w)] for _ in range(h)]
