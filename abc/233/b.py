# input
l, r = [int(_) - 1 for _ in input().split()]
s = str(input())

ans = ""
for i in range(len(s)):
    if l <= i <= r:
        idx = r - (i - l)
        ans += s[idx]
    else:
        ans += s[i]
print(ans)
