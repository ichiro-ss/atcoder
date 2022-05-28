# input
h, w = [int(_) for _ in input().split()]
s = [[str(_) for _ in list(input())] for _ in range(h)]

p = []
for i in range(h):
    for j in range(w):
        if s[i][j] == "o":
            p.append(i)
            p.append(j)
print(abs(p[0] - p[2]) + abs(p[1] - p[3]))