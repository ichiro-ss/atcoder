# input
n, k = [int(i) for i in input().split()]
s = []
for _ in range(n):
    s.append([str(i) for i in list(input())])

# brute force of bit key
ans = 0
for bits in range(2 ** n):
    cnt = 0
    exist = {}
    for i in range(n):
        if ((bits >> i) & 1):
            for c in s[i]:
                if c in exist:
                    exist[c] += 1
                else:
                    exist[c] = 1
    for key in exist:
        if exist[key] == k:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)