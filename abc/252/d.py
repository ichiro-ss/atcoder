# input
n = int(input())
a = [int(_) for _ in input().split()]

LIMIT = 2 * 10 ** 5

cnt = [0] * (LIMIT + 1)
for i in range(n):
    cnt[a[i]] += 1

for i in range(LIMIT):
    cnt[i + 1] += cnt[i]

ans = 0
for j in range(n):
    ans += cnt[a[j] - 1] * (n - cnt[a[j]])
print(ans)