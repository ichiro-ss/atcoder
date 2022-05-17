# input
h, w = [int(_) for _ in input().split()]
c = [str(input()) for _ in range(h)]

scores = [[0 for _ in range(w+1)] for _ in range(h+1)]
for i in range(h-1, -1, -1):
    for j in range(w-1, -1, -1):
        if c[i][j] == "#":
            continue
        scores[i][j] = max(scores[i+1][j], scores[i][j+1]) + 1
print(scores[0][0])
