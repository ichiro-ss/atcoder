# input
n = int(input())
h = [int(_) for _ in input().split()]

pos, height = 0, h[0]
while pos < n - 1:
    if height < h[pos + 1]:
        pos += 1
        height = h[pos]
    else:
        break
print(height)
