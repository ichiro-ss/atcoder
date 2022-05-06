# input
x, y = [int(i) for i in input().split()]

ans = "No"
for i in range(x + 1):
    if i * 2 + (x - i) * 4 == y:
        ans = "Yes"
print(ans)