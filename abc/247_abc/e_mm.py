# input
from re import X


n, x, y = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

def calc(b):
    i, j, countX, countY, res = 0, 0, 0, 0, 0
    while i != len(b):
        while j != len(b) and (countX == 0 or countY == 0):
            if b[j] == x:
                countX += 1
            if b[j] == y:
                countY += 1
            j += 1
        if countX > 0 and countY > 0:
            res += len(b) + 1 - j
        if b[i] == x:
            countX -= 1
        if b[i] == y:
            countY -= 1
        i += 1
    return res
    
i, ans = 0, 0
while i != n:
    b = []
    while i != n and y <= a[i] <= x:
        b.append(a[i])
        i += 1
    if len(b) != 0:
        ans += calc(b)
    else:
        i += 1
print(ans)