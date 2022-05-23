# input
s = str(input())
a, b = [int(_) for _ in input().split()]

for i in range(len(s)):
    if i == a-1:
        print(s[b-1], end = "")
    elif i == b-1:
        print(s[a-1], end = "")
    else:
        print(s[i], end = "")