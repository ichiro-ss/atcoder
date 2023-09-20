# input
n = int(input())
a, b = [0]*n, [0]*n
for i in range(n):
    a[i], b[i] = [int(j) for j in input().split()]

# brute force O(n^3)
for k in range(1, n * 2 + 1):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i + j + 2 == k:
                cnt += a[i] * b[j]
    print(cnt)

# modified brute force O(n^2)
for k in range(1, n * 2 + 1):
    cnt = 0
    for i in range(n):
        j = k - i - 2
        if 0 <= j < n:
            cnt += a[i] * b[j]
    print(cnt)

# Fast fourier transformation
