# input
n = int(input())
s, t = [], []

for _ in range(n):
    a, b = [_ for _ in input().split()]
    s.append(str(a))
    t.append(int(b))

origin = [False for _ in range(n)]
seen = set()
for i in range(n):
    if s[i] not in seen:
        seen.add(s[i])
        origin[i] = True

max_v = 0
ans = 0
for i in range(n):
    if origin[i] and max_v < t[i]:
        ans = i
        max_v = t[i]
print(ans + 1)