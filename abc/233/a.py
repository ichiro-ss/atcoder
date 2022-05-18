# input
x, y = [int(_) for _ in input().split()]

cnt = 0
while x < y:
    x += 10
    cnt += 1
print(cnt)