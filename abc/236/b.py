# input
n = int(input())
a = [int(_) for _ in input().split()]

cnts = [0 for _ in range(n)]
for i in range(4 * n - 1):
    cnts[a[i] - 1] += 1
for i in range(n):
    if cnts[i] < 4:
        print(i+1)