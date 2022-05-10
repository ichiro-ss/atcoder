# input
n = int(input())
a = [int(_) for _ in input().split()]

# brute force O(n^2)
# cnt = 0
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if a[i] != a[j]:
#             cnt += 1
# print(cnt)

cnts = {}
ans = 0
for i in range(n):
    if a[i] not in cnts:
        cnts[a[i]] = 0
    ans += (i - cnts[a[i]])
    cnts[a[i]] += 1
print(ans)
