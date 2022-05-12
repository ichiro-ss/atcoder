# input
a, b, c, d = [int(_) for _ in input().split()]

blue, red = a, 0
ans = -1
for i in range(a + 1):
    if blue <= d * red:
        ans = i
        break
    blue += b
    red += c
print(ans)
