# input
n = int(input())
h = [int(_) for _ in input().split()]

pos, height = 0, h[0]
for i in range(1, n):
    if height < h[pos + 1]:
        pos += 1
        height = h[pos]
    else:
        break
print(height)
