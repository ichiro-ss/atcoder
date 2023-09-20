# input
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

minv = a[0]
mini = -1
ans = -1
for i in range(k):
    if a[i] <= minv:
        minv = a[i]
        mini = i

for i in range(k, n):
    if minv < a[i]:
        ans = i - mini
        break

print(ans)