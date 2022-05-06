# input()
n = int(input())
s, t = [], []
for i in range(n):
    a, b = [str(i) for i in input().split()]
    s.append(a)
    t.append(int(b))

if t[1] < t[0]:
    max_id, max_v = 0, t[0]
    max2_id, max2_v = 1, t[1]
else:
    max_id, max_v = 1, t[1]
    max2_id, max2_v = 0, t[0]

for i in range(2, n):
    if max_v < t[i]:
        max2_id, max2_v = max_id, max_v
        max_id, max_v = i, t[i]
    elif max2_v < t[i]:
        max2_id, max2_v = i, t[i]
print(s[max2_id])